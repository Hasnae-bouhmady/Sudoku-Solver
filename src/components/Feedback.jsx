import React, {useState, useEffect} from 'react';
import "./App.css"


function FeedBack() {
    const [message, setMessage] = useState([]);
    const [image, setImage] = useState([]);
    const [isImage, setIsImage] = useState(false);
    useEffect(() => {
        async function fetchAPI() {
            let response  = await fetch('http://127.0.0.1:5000/solution', {
                method : "GET",
                 headers : {
                     'Accept': 'application/json'
                 }
            })
            const blob = await response.blob();
            setImage(URL.createObjectURL(blob));
            setIsImage(true);
        }
        fetchAPI()
    },[])
    if (isImage){
        return (
           <div className="feedback">
           <br/>
           <img src={image} />
           </div>
        );
    }else{
        return (
           <div className="feedback">
           <label>{message.status}</label>
           <br/>
           </div>
        );
    }
}


export default FeedBack;