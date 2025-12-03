
import "./svg-hover.css"
import { motion, useMotionValue } from 'framer-motion'
import { useRef, useState, useEffect } from "react"

export default function SvgHover() {

    // const percentX = useMotionValue(0)
    // const percentY = useMotionValue(0)
    const [percentX, setPercentX] = useState(0)
    const [percentY, setPercentY] = useState(0)
    const divRef = useRef(null)
    const [onSvg, setOnSvg] = useState(false)
    const divRect = useRef(null)
    useEffect(() => {
        divRect.current = divRef.current.getBoundingClientRect()
    }, [divRef])

    function handleMouseMove(event) {
        if (onSvg) {
            console.log("mouse move")


            setPercentX((event.clientX - divRect.current.left) / divRect.current.width * 100)
            setPercentY((event.clientY - divRect.current.top) / divRect.current.height * 100)

            console.log(percentX)
            console.log(percentY)
        }
    }

    return (
        <div ref={divRef} className="svg-div" onMouseEnter={() => setOnSvg(true)} onMouseLeave={() => setOnSvg(false)} onMouseMove={handleMouseMove}>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                className="svg-to-hover"

            >

                <defs>
                    <radialGradient
                        id="emeraldGradient"
                        gradientUnits="userSpaceOnUse"
                        r="35%"
                        cx={`${percentX}%`}
                        cy={`${percentY}%`}

                    >
                        {onSvg && <stop offset="0%" stopColor="#f04d4d" />}
                        <stop offset={1} stopColor="#FFFFFF" />
                    </radialGradient>
                </defs>
                {/*svg is below */}
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"  
                        className="path outer"
                        stroke="url(#emeraldGradient)"
                        d="M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.047 8.287 8.287 0 0 0 9 9.601a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z"
                    />
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="path inner"
                        stroke="url(#emeraldGradient)"
                        d="M12 18a3.75 3.75 0 0 0 .495-7.468 5.99 5.99 0 0 0-1.925 3.547 5.975 5.975 0 0 1-2.133-1.001A3.75 3.75 0 0 0 12 18Z"
                    />
                
            </svg>

        </div>

    )
}