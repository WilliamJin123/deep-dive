import { Link } from "react-router-dom"
import { motion } from "framer-motion";
import { buttonVariant, containerVariant, homePageVariant } from "./animations";
import { Loader } from "./loader";

export default function Home(){


    return(
        <motion.div className="home page"
            variants={containerVariant}
            exit="exit"

        >
            <motion.h2
            variants={{...containerVariant}}
            initial="hidden"
            animate="visible"
            >Welcome to the Pizza Joint </motion.h2>
            <Link to="/base">
                <motion.button
                    variants={{...containerVariant, ...buttonVariant, ...homePageVariant,}}
                    initial={{
                        opacity:0,
                        scale:0.1,
                    }}
                    animate="visible"
                    
                    whileHover="whileHover"
                    whileTap="whileTap"
                    
                >
                    Create Your Pizza
                </motion.button>
            </Link>
            <Loader />
        </motion.div>
    )
}