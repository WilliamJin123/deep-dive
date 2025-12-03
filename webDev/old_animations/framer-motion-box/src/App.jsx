import "./App.css"
import { useState } from "react"
import { motion } from "framer-motion"
import Input from "./input"
export default function App(){

  const [x, setX] = useState(0)
  const [y, setY] = useState(0)
  const [rotate, setRotate] = useState(0)
  return(
    <div className="example">
      <div>
        <motion.div
          className="box"
          animate={{ x, y, rotate }}
          transition={{ type: "spring", stiffness: 50 }}
        />
      </div>
      <div className="inputs">
        <Input value={x} onChange={setX}>
        x
      </Input>
      <Input value={y} onChange={setY}>
        y
      </Input>
      <Input value={rotate} onChange={setRotate}>
        rotate
      </Input>
      </div>
      
    </div>
  )
}