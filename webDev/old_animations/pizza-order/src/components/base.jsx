
import { Link } from "react-router-dom"
import { motion } from "framer-motion"

import { pageVariant, listItemVariant, buttonVariant, defaultVariant, containerVariant} from "./animations"


const nextVariant ={
    initial:{
        x:'-100vw',

    },
    animation:{
        x:0,

    }
}
export default function Base({addBase, pizza}){
    const bases = ['Classic', 'Thin & Crispy', 'Thick Crust']
    const basesList = bases.map((base, index) => (
        <motion.li key={index} onClick={() => addBase(base) } className={pizza.base === base? 'active' : ''}
            
            variants={listItemVariant}
            whileHover="whileHover"
            
        >{base}</motion.li>
    ))
    return(
        <motion.div className="bases page"
            variants={{...pageVariant, ...defaultVariant, ...containerVariant}}
            initial="initial"
            animate="animation"
            transition={{
                ...defaultVariant.transition,
                }}
            exit="exit"
        >
            <h3>Step 1: Choose Your Base</h3>
            <motion.ul
                variants={listItemVariant}
                transition={{
                    type:'spring',
                    stiffness:50,
                    delay:0,
                    mass:0.4,
                    damping: 8,
                    staggerChildren:0.4,
                }}
            >
                {basesList}
            </motion.ul>
            {pizza.base && (
                <motion.div className="next"
                    variants={{...nextVariant, ...defaultVariant}}
                    transition={defaultVariant.transition}
                >

                <Link to="/toppings">
                    <motion.button
                        variants={buttonVariant}
                        whileHover="whileHover"
                        whileTap="whileTap"
                    >Next</motion.button>
                </Link>
                </motion.div>
            )}
        </motion.div>
    )
}