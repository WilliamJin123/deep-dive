import { useEffect, useState, useRef } from "react";
import { useAnimate, motion, useInView,  useAnimationControls} from "framer-motion";

export default function Reveal({ children }) {

    const [scope, animate] = useAnimate();

    const viewRef = useRef(null);
    const isInView = useInView(viewRef, {threshold: 0.1, once:true});

    

    useEffect(() => {
        const animateElement = () => {
            if (isInView){
            animate(".reveal-green-box", {left:"200%"},{duration:0.6, delay: 0.1, ease:"easeIn"});
            animate(".reveal-animation", {opacity:1, y:0}, {duration: 0.5, delay: 0.25});
        }
        }
        animateElement();

    }, [isInView, animate])

    // const slideControls = useAnimationControls();
    // const revealControls = useAnimationControls();
    // useEffect(() => {
       
        
    //     if (isInView){
    //         slideControls.start("visible");
    //         revealControls.start("visible");
    //     }

    //     return () => {
    //         slideControls.stop();
    //         revealControls.stop();
    //     }
    // }, [isInView])


    return (
        <div className="reveal" ref={scope}>
            <motion.div ref={viewRef}
                // variants={{visible:{
                //     opacity: 1,
                //     y: 0,
                // }}}
                className="reveal-animation"
                initial={{
                    opacity: 0,
                    y:20,
                }}
                // animate={revealControls}
                // whileInView={{opacity: 1, y: 0, }}
                // transition={{duration: 0.5, delay: 0.25}}
                // viewport={{once:true}}

            >
                {children}
            </motion.div>
            <motion.div className="reveal-green-box"
                // variants={{visible:{left:'200%'}}}
                initial={{left:0}}
                // animate={slideControls}
                // transition={{duration:0.6, delay: 0.1, ease:"easeIn"}}
                />
        </div>

    )
}