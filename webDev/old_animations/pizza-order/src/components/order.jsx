import { motion, AnimatePresence} from "framer-motion"
import { pageVariant, childVariant, containerVariant} from "./animations"

import { useState, useEffect } from "react"

export default function Order({ pizza, setShowModal }) {
    // const [showTitle, setShowTitle] = useState(true)

    useEffect(() => {
        const timer= setTimeout(()=>{
            setShowModal(true)
        }, 4000)
        
        return () => clearTimeout(timer)
    })
    

    return(

        <motion.div className="order page"
            variants={{...pageVariant, ...containerVariant}}
            initial="initial"
            animate="animation"
            exit="exit"
        >
            
            <h2>Thank you for the order</h2>
            
            
            {pizza.toppings.length > 0?
                <>
                    <motion.p variants={childVariant}>You ordered a {pizza.base} pizza with: </motion.p>
                    <motion.div variants={childVariant}>
                        {pizza.toppings.map(topping => (
                            <motion.div key={topping} variants={childVariant}>
                                {topping}</motion.div>
                        ))}
                    </motion.div>
                    
                </>
                
                :
                <motion.p variants={childVariant}>You ordered a {pizza.base}pizza</motion.p>
                
            }
            
        </motion.div>
    )
}