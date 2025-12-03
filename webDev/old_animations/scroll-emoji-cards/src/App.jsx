import { useState } from 'react'
import './App.css'
import {motion} from 'framer-motion'
const food = [
  ["🍅", 340, 10],
  ["🍊", 20, 40],
  ["🍋", 60, 90],
  ["🍐", 80, 120],
  ["🍏", 100, 140],
  ["🫐", 205, 245],
  ["🍆", 260, 290],
  ["🍇", 290, 320]
];

const cardVariants = {
  offscreen: {
    y:300
  },
  onscreen: {
    y:50,
    rotate:-10,
    transition: {
      type: "spring",
      bounce: 0.4,
      duration: 0.8
    }
  }
}

function hue(degrees) {
  return `hsl(${degrees}, 100%, 50%)`;
}

function Card({emoji, hueA, hueB}) {
  const background = `linear-gradient(306deg, ${hue(hueA)}, ${hue(hueB)})`;

  return(
    <motion.div className='card-container'initial="offscreen" whileInView="onscreen" viewport={{once: true, amount: 0.8}}>
      <div className='splash' style={{background}}/>
      <motion.div className='card' variants={cardVariants}>{emoji}</motion.div>
    </motion.div>
  )
}

function App() {
  

  return (
    <div>
      {food.map(([emoji, hueA, hueB], index) => (
        <Card key={index} emoji={emoji} hueA={hueA} hueB={hueB}/>
      ))}
    </div>
  )
}

export default App
