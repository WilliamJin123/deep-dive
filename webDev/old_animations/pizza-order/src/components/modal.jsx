import { motion, AnimatePresence } from "framer-motion";
import { Link } from "react-router-dom";
import { backdropVariant, buttonVariant, containerVariant, homePageVariant } from "./animations";

export default function Modal({showModal, setShowModal})  {
    return(
        <AnimatePresence mode="wait">
            {showModal && (
                <motion.div className="backdrop"
                    variants={{...containerVariant, ...backdropVariant}}
                    initial="hidden"
                    animate="visible"
                    exit="exit"
                    transition={{
                        duration:5
                    }}
                >
                    <motion.div className="modal"
                        initial={{
                            y:'100vh'
                        }}
                        animate={{
                            y:0,
                            transition:{
                                type:'spring',
                                stiffness:50,
                                delay:0
                            }
                        }}
                    >
                        <p>Want to make another pizza?</p>
                        <Link to="/">
                            <motion.button
                                variants={{...containerVariant, ...buttonVariant}}
                                initial="initial"
                                animate={{
                                    ...containerVariant.visible,
                                    transition:{
                                        ...containerVariant.visible.transition,
                                        delay:0
                                    }
                                    
                                }}
                                whileHover="whileHover"
                                whileTap="whileTap"
                                onClick={() => setShowModal(false)}
                            >Start Again</motion.button>
                        </Link>
                    </motion.div>
                </motion.div>

            )}
        </AnimatePresence>
    )
}
