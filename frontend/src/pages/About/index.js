import React  from 'react';
import { Container, Paragraph } from './styles'
import {
  Link,
} from "react-router-dom"



function About() {

    return (
      <Container>
        <div className="nine columns main-col" style={{width: '100%', minHeight: '75vh', maxWidth: '1024px'}}>
           <h2>About</h2>

           <Paragraph> To be continued... </Paragraph>


        </div>
      </Container>

    );
}

export default About;
