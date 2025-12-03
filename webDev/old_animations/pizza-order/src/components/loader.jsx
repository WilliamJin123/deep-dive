import { motion, useCycle } from "framer-motion"
import { loaderVariant } from "./animations"

export function Loader() {
    const [animation, cycleAnimation] = useCycle("animationOne","animationTwo")


    return(
        <>
        <motion.div className="loader"
            variants={loaderVariant} animate={animation}
        >

        </motion.div>
        <div onClick={cycleAnimation} style={{cursor:'pointer'}}>
            Cycle Loader
        </div>

        </>
    )
}