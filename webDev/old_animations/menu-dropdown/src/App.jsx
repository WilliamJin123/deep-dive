import "./App.css"
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion"
import { buttonVariants, itemVariants, listVariants, svgVariants } from "./variants";
export default function App() {
  const [open, setOpen] = useState(false)
  const itemList = [];
  for (let i = 1; i <= 6; i++) {
    itemList.push(`Item ${i}`)
  }
  const itemListDisplay = itemList.map((item, index) => (
    <motion.li key={index} variants={itemVariants} custom={index}>
      {item}
    </motion.li>
  ))
  return (
    <motion.div className='main-div'
      initial={open}
      animate={open ? "open" : "closed"}
    >
      <motion.button className='main-button' onClick={() => setOpen(!open)}
        variants={buttonVariants}
        whileTap="whileTap"

      >Menu

        <div className='svg-div'>
          <motion.svg width="15" height="15" viewBox="0 0 20 20"
            variants={svgVariants}
            transition="transition"
          >
            <path d="M0 7 L 20 7 L 10 16" />
          </motion.svg>
        </div>

      </motion.button>
      <AnimatePresence
        
      >
        {open && (<motion.ul 
          variants={listVariants}
          initial="closed"
          animate="open"
          
          exit="closed"
          className={`item-list`}
        >
          {itemListDisplay}
        </motion.ul>
        )}
        

      </AnimatePresence>


    </motion.div>
  )
}