import { useRef } from "react"
import { defaultVariant, pathVariant, svgVariant } from "./animations"
import { motion } from "framer-motion"

export default function Header(){
    const constraints = useRef(null)
    return(
        <header ref={constraints}>
      <motion.div className="logo" 
        drag
        dragConstraints={constraints}
        dragElastic={1}
        style={{cursor:'pointer'}}
      >
        <motion.svg className="pizza-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"
          variants={svgVariant} initial="initial" animate="animate"
        >
          <motion.path
            fill="none"
            d="M40 40 L80 40 C80 40 80 80 40 80 C40 80 0 80 0 40 C0 40 0 0 40 0Z"
            variants={pathVariant}
          />
          <motion.path
            fill="none"
            d="M50 30 L50 -10 C50 -10 90 -10 90 30 Z"
            variants={pathVariant}
          />
        </motion.svg>
      </motion.div>
      <motion.div className="title"
        variants={defaultVariant}
        initial={{
          y:-250,

        }}
        animate={{
          y:-10,

        }}
        transition={{
          ...defaultVariant.transition,
          
        }}
      >
        <h1>Pizza Joint</h1>
      </motion.div>
    </header>
    )
}