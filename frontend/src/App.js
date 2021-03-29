import React from 'react';
// ,{ useState, useEffect } from 'react';
import './App.css';
import { MetaContainer } from './styles'
import Home from './pages/Home'
import Navbar from './components/NavBar'
import {
  Switch,
  Route
} from "react-router-dom"
import About from './pages/About';
import Footer from './components/Footer';


function App() {


  return (
    <MetaContainer>
          <Navbar/>
            <Switch>
             <Route exact path="/" component={Home} />
             <Route path="/about" component={About}  />
           </Switch>
      <Footer />
    </MetaContainer>
  );
}

export default App;
