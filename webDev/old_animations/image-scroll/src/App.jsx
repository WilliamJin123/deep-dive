import "./App.css";
import {flushSync} from "react-dom";
import { useState, useRef,  } from "react";

const imageList = []
for (let i = 0; i<10; i++){
  imageList.push({
    id: i,
    imageUrl: `https://picsum.photos/2500/1600?random=${i}`
  })
}
export default function App(){
  const selectedRef = useRef(null);
  const[index, setIndex] = useState(0);
  
  return(
    <div className="main">
      <button
        onClick={e => {
          flushSync(() => {
            if(index < imageList.length-1){
              setIndex(index+1)
            }else{
              setIndex(0)
            }
          })
          console.log(index)
          selectedRef.current.scrollIntoView({
            behavior: 'smooth',
            block: 'nearest',
            inline: 'center'
          })
        }}

      >Next</button>
      
        <ul className="img-list">
        {imageList.map(item => (
          <li
            key={item.id}
            ref = {item.id === index? selectedRef : null}
          ><img 
            src={item.imageUrl}
            className={item.id === index? "active" : ""}
            ></img></li>
        ))}
      </ul>
      
    </div>
  )
}