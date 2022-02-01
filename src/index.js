import React from 'react';
import ReactDOM from 'react-dom';
import Footer from './components/Footer.jsx';
import Header from './components/Header.jsx';
import Upload from './components/upload.jsx';
import FeedBack from './components/Feedback.jsx';
import InfoDisplay from './components/info.jsx';
import Logo from './components/Logo.jsx';
import "./index.css"

ReactDOM.render(
    <div className="home">
    <Header/>
    <InfoDisplay/>
    <Logo/>
    <Upload/>
    <FeedBack/>
    <Footer/>
    </div>,
  document.getElementById('root')
);
