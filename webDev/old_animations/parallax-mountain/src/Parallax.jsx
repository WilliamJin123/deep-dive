import { motion, useScroll, useTransform } from "framer-motion"
import { useRef } from "react";

export default function Parallax() {
    const ref = useRef(null);
    const {scrollYProgress} = useScroll({
        target: ref,
        offset: ["start start", "end start"]
    })

    const backImgY = useTransform(scrollYProgress, [0,1], ['0%', '100%'])
    const textY =  useTransform(scrollYProgress, [0,1], ['0%', '300%'])
    return(
        <div ref={ref} className="parallax"
        >
            <motion.h1 style={{y: textY}}>PARALLAX</motion.h1>
            <motion.div className="bg-img" style={{y: backImgY}}>
            </motion.div>
            <div className="front-img" style={{y:backImgY}}>

            </div>
            

        </div>
    )
}