
//import './App.css';

import Navbar from './component/Navbar'
import Textbox from './component/Textbox'
import React, { useState } from 'react';
import Card from './component/card';


function App() {
 const [mode,setMode]=useState('light');
 const toggleMode= ()=>{
  if(mode==='light'){
    setMode('dark');
    document.body.style.backgroundColor='rgb(53, 48, 40)';
    document.body.style.color='white';
  }
  else{
    setMode('light');
    document.body.style.backgroundColor='white';
  }
 }
  return (
    <>   
     <Navbar title="TextUtils" mode={mode} toggleMode={toggleMode}/>
     <Textbox  heading="Analyze Your Text Here"/>
     
      </>
  )
}

export default App;
