import { useEffect, useRef, useState } from "react";
import { motion, AnimatePresence, useScroll, useTransform, useAnimate, useSpring } from "framer-motion";


const imgList = []
for (let i = 0; i < 8; i++) {
    imgList.push(`../../public/img-${i + 1}.jpg`)
}

export default function Track() {


    const divRef = useRef(null);
    const { scrollYProgress } = useScroll({ target: divRef });
    const [scope, animate] = useAnimate();
    const [isPanning, setIsPanning] = useState(false);


   


    // useEffect(() => {
    //     const updateScrollPercent = () => {
    //         if (divRef.current) {
    //             let scrollWidth = divRef.current.scrollWidth;
    //             let vwWidth = window.innerWidth * 0.5 - window.innerHeight * 0.16;
    //             let percentage = (vwWidth / scrollWidth) * 100;
    //             scrollPercent.current = percentage / 2;
    //         }
    //     };

    //     updateScrollPercent(); 

    // }, []);

    const [trackX, setTrackX] = useState("21.3%");
    const [imageX, setImageX] = useState("100%");
    const springX = useSpring(scrollYProgress, { stiffness: 200, damping:75 })
    const transformX = useTransform(springX, [0, 1], [`21.3%`, `-67.1%`]);
    const transformImgX = useTransform(springX, [0, 1], [`100%`, `0%`]);
    
    
    const [height, setHeight] = useState('auto');
    const [opacity, setOpacity] = useState(0);
    
    useEffect(() => {
        if (!isPanning) {
            setTrackX(transformX);
            setImageX(transformImgX);
            console.log("changes occuring");
        }

        console.log(scrollYProgress.get())

    }, [scrollYProgress, isPanning])

    // useEffect(()=>{
    //     animate(".img-list", {x:`${transformX}`}, {duration:0.12, ease:'easeInOut'})
    //     console.log("play anim")
    // }, [scrollYProgress, animate])

    useEffect(() => {
        const updateHeight = () => {
            if (divRef.current) {
                const width = divRef.current.scrollWidth;
                setHeight(`${width * 5}px`)
                setOpacity(1)
            }
        }
        updateHeight();
        window.addEventListener('resize', updateHeight)

        return () => window.removeEventListener('resize', updateHeight)
    }, [])


    const [curScroll, setCurScroll] = useState(scrollYProgress.get())
    const panWidth = window.innerWidth/2;
    const prevOffset = useRef(0)
    const prevDir = useRef(0)
    function handlePanStart() {
        setIsPanning(true)
        console.log("panning start")
        prevOffset.current = 0
        prevDir.current = 0
        setCurScroll(scrollYProgress.get())
    }
    function handlePanEnd(event, panInfo) {
        console.log("panning end")
       
        const newProgress = Math.max(
            Math.min(1, curScroll - (panInfo.offset.x - prevOffset.current) / panWidth),
            0
        )

        const newScrollPosition = newProgress * (divRef.current.scrollHeight - window.innerHeight)
        window.scrollTo({
            top: newScrollPosition,
            behavior: 'auto'
        })
        prevOffset.current = 0
        prevDir.current = 0
        setIsPanning(false)
    }
    function handlePan(event, panInfo) {
        if (!isPanning) return;
        const curOffset = panInfo.offset.x
        const curDir = Math.sign(curOffset - prevOffset.current)
        
        const newProgress = Math.max(
            Math.min(1, curScroll - (panInfo.offset.x - prevOffset.current) / panWidth),
            0
        )
        scrollYProgress.set( newProgress)
        

        if (curDir !== prevDir.current){
            prevOffset.current = curOffset
            console.log(`${prevDir.current} ${prevOffset.current} ${curDir}`)
        }
        prevDir.current = curDir
    }

    // const handleDrag = (event, info) => {
    //     const dragWidth = divRef.current.scrollHeight*2;
    //     const progressOffset = info.offset.x / dragWidth;
    //     const newProgress = Math.max(0, Math.min(1, scrollYProgress.get() - progressOffset));
    //     scrollYProgress.set(newProgress);
    // };

    return (
        <motion.div className="img-track-div" ref={divRef} style={{ height, width: '100%', }} 
            onPanStart={handlePanStart}
            onPan={handlePan}
            onPanEnd={handlePanEnd}
            // drag="x"
            // dragConstraints={{ left: -window.innerWidth, right: window.innerWidth }}
            // dragElastic={0.2}
            // onDrag={handleDrag}
            >
            <div className="img-track" ref={scope}>
                <motion.ul className="img-list" initial={{ x: '21.3%' }} style={{ x: trackX }} 
                    transition={{
                        type: "tween",
                        ease: "linear",
                        duration: 0
                    }}
                >
                    {imgList.map((image, index) => (
                        <li key={index} ><motion.img layout src={image} style={{ objectPosition: imageX, opacity }} 
                        transition={{
                            type: "tween",
                            ease: "linear",
                            duration: 0
                        }}
                        /></li>
                    ))}
                </motion.ul>

            </div>
        </motion.div>
    )



}