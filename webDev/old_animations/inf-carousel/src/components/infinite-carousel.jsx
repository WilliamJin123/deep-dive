import { useRef, useState, useEffect } from "react";
import "./infinite-carousel.css"
import Arrow from "./arrow.svg"
import { motion, AnimatePresence, useMotionValue, useAnimate } from "framer-motion";
const images = [
    "/image-1.jpg",
    "/image-2.jpg",
    "/image-3.jpg",
    "/image-4.jpg",
    "/image-5.jpg",
    "/image-6.jpg",
    "/image-7.jpg",
    "/image-8.jpg",
];

function Card({ image }) {

    const [showOverlay, setShowOverlay] = useState(false)
    return (
        <motion.div className="inf-img-container" onHoverStart={() => setShowOverlay(true)} onHoverEnd={() => setShowOverlay(false)}>
            <AnimatePresence> {showOverlay && (

                <motion.div className="overlay" >
                    <motion.div className="overlay-bg"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 0.5 }}
                        transition={{ duration: 0.15 }}
                        exit={{ opacity: 0, transition: { duration: 0.15 } }} />

                    <motion.h1
                        initial={{ opacity: 0, y: 15 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.15 }}
                        exit={{ opacity: 0, y: 15, transition: { duration: 0.3 } }}
                    ><span>Explore Now</span>
                        <img src={Arrow} alt="Arrow Icon" className="arrow" />
                    </motion.h1>
                </motion.div>

            )}  </AnimatePresence>
            <img className="inf-img" src={image} alt={image} />
        </motion.div>

    )
}

export default function InfiniteCarousel() {
    const [scope, animate] = useAnimate()
    const carouselRef = useRef(null)
    const carouselWidth = useRef(0)
    const imagesRender = [...images, ...images].map((image, index) => (
        <Card key={index} image={image} />
    ))

    useEffect(() => {
        if (carouselRef.current) {
            carouselWidth.current = carouselRef.current.offsetWidth
        }
    }, [])


    const translateX = useMotionValue(0)
    const FAST = 25;
    const SLOW = 75;
    const [duration, setDuration] = useState(FAST)
    const [mustFinish, setMustFinish] = useState(false)
    const [rerender, setRerender] = useState(false)

    useEffect(() => {
        let finalPosition = (-carouselWidth.current - 16) / 2
        let controls;
        if (mustFinish) {
            controls = animate(translateX, [translateX.get(), finalPosition], {
                ease:'linear',
                duration: duration* (1-translateX.get() / finalPosition),
                repeat:Infinity,
                repeatType: 'loop',
                repeatDelay: 0,
                onComplete: () => {
                    setMustFinish(false)
                    setRerender(false)
                }
            })
        } else {
            controls = animate(translateX, [0, finalPosition], {
                ease: 'linear',
                duration,
                repeat: Infinity,
                repeatType: 'loop',
                repeatDelay: 0,
            })
        }
        return () => controls.stop;
    }, [translateX, carouselWidth, duration, rerender])

    return (
        <motion.div className="inf-carousel" ref={carouselRef} style={{ x: translateX }}
            onHoverStart={() => {
                
                setDuration(SLOW)
                setMustFinish(true)
            }}
            onHoverEnd={() => {
                
                setDuration(FAST)
                setMustFinish(true)
            }}
        >
            {imagesRender}
        </motion.div>
    )
}