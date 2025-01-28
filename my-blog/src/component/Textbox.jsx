import React, {useState} from 'react'

export default function Textbox(props){
    const [text,setText]=useState("Enter Text Here");
    const upperclick= () => {
        console.log("button was clicked");
        let next=text.toUpperCase();
        setText(next);
        
    }

    const lowerclick= () => {
        console.log("button was clicked");
        let next=text.toLowerCase();
        setText(next);
        
    }
    const copy= () => {
        var text=document.getElementById("mybox");
        text.select()
        navigator.clipboard.writeText(text.value);
        
    }
    const capitalise=()=>{
      let change= text.split(' ').map(text=>text.charAt(0).toUpperCase() + text.slice(1).toLowerCase()).join(' ');
      setText(change);
    }
    const change=(event) =>{
        console.log("Changed");
        setText(event.target.value);
    }


    return(
        <>
        <div>
            <h1>{props.heading}</h1>
            <div>
            <textarea  className='container mx-6 my-3' value={text} onChange={change} rows="8" id="mybox"></textarea>
            </div>
            <div >
            <button className='btn btn-success mx-2 my-3' onClick={upperclick} >Change To UpperCase</button>
            <button className='btn btn-warning mx-2 my-3' onClick={lowerclick} >Change To LowerCase</button>
            
            <button className='btn btn-danger mx-2 my-3' onClick={capitalise} value={text}>Change To SentenceCase</button>
            <button className='btn btn-primary mx-2 my-3' onClick={copy} value={text}>Copy</button>
            
            </div>
            <h1>Preview</h1>
                <p>{text.split(" ").filter((element)=>{
                    return element!=0
                }).length} words {text.length} character</p>
                 <p>{0.008*text.length} minute read</p>
                 <h4>Your Input Text</h4>
                <p>{text}</p>
                
            </div>
    
            </>
           
    );
}