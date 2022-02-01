import React from 'react';
import "./App.css"

function Footer(){
    let currentYear= new Date().getFullYear()
    return (<footer>
    <p>© copyright {currentYear}</p>
    </footer>
    );
};

export default Footer;