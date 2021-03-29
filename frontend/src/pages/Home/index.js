import React, { useState, } from 'react';
import { Button, Details, AboutDescription,
      Container, Input, TextArea } from './styles'
// import { Link, } from 'react-router-dom';
import Spinner from '../../components/Spinner'
import '../../global.js'
import SearchBar from "../../components/Search";
import FadeIn from "../../components/FadeIn"
import TextCard from "../../components/Cards"


function Home() {
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [summaryText, setSummaryText] = useState("");
  const [company, setCompany] = useState('');

  const summarize = async text => {
    setSuccess(false)

    if (text !== "")
      setLoading(true);
    const data = {'text': text}
    const settings = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    };
    const response = await fetch(process.env.REACT_APP_LOCAL_TBD_API + '/get_info', settings);
    // const response = await fetch('/get_article', settings);
    const summary = await response.json();
    setLoading(false)
    setSuccess(true)
    setSummaryText(summary.output);
  }

  const Display = (summary) => {
      var json = summary;
      var new_dict = [];
      var counter = 0;
      Object.keys(json.summary).forEach(function(key) {
        new_dict.push({"title": key, "sentences": json.summary[key].slice(1), "description": json.summary[key][0],"duration": 1300 + counter});
        counter = counter + 200;
      });

      return (
        <ul>{new_dict.map(item => <FadeIn duration={item.duration}><TextCard title={item.title} text={item.sentences} description={item.description}></TextCard></FadeIn>)}</ul>
      );

  };


  return (
      <div style={{ width: '100%', minHeight: '75vh', maxWidth: '1024px' }}>
        <AboutDescription>
          <FadeIn>
            <div>
              <Details>Generate summaries of risk analysis for the latest 10-ks.
                  </Details>
              <Container>
                <Input name='text' cols="120" placeholder="Company Name or CIK..." value={company} onChange={event => setCompany(event.currentTarget.value)}></Input>
              </Container>
              <Container>
                <Button onClick={() => summarize(company)}>Generate Summary</Button>
                {loading ? <Spinner /> : <br />}
              </Container>
            </div>
          </FadeIn>
        </AboutDescription>
        {success ?  <Display summary={summaryText}/>: <br />}
      </div>
  );
}

export default Home
