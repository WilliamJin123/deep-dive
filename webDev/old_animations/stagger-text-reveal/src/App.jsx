import { useState } from 'react'
import './App.css'
import { motion } from 'framer-motion'


const duration = 0.25
const stagger = 0.025
function FlipLink({href, children}){

  return(
    <motion.a href={href}
      initial="initial"
      whileHover="hovered"
      // transition={{staggerChildren:0.2}}  
      // takes all letters off screen for first div then the rest of the letters for the next div come in
    >
    <div>{children.split("").map((letter, index) => (<motion.span key={index}
      variants={{initial:{y:0}, hovered:{y:'-101%'}}} 
      transition={{duration, ease:"easeInOut", delay: stagger*index}} 
      // animates each letter in and out individually, instead of having a delay on the second div
    >{letter}</motion.span>))}</div>
    <div className='animation-text'>{children.split("").map((letter, index) => (<motion.span key={index}
      variants={{initial:{y:'100%'}, hovered:{y:0}}} 
      transition={{duration, ease:"easeInOut", delay: stagger*index}}
      // animates each letter in and out individually, instead of having a delay on the second div
    >{letter}</motion.span>))}</div>
    </motion.a>
  )
}

function App() {
  
  return (
    <div className='main'> 
        <FlipLink href="#">Twitter</FlipLink>
        <FlipLink href="#">Linkedin</FlipLink>
        <FlipLink href="#">Facebook</FlipLink>
        <FlipLink href="#">Instagram</FlipLink>
    </div>
  )
}

export default App
