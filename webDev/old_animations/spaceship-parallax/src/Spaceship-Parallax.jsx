import "./Spaceship-Parallax.css"
import React, { useRef } from "react"
import { SiSpacex } from "react-icons/si"
import { FiArrowRight } from "react-icons/fi"
import { motion, useScroll, useTransform, useMotionTemplate } from "motion/react"
import { ReactLenis } from "lenis/dist/lenis-react.mjs"
export default function SpaceshipParallax() {

    return (
        <div className="main-div">
            <ReactLenis root options={{lerp:0.05}}>
                <Nav />
                <Hero />
            </ReactLenis>


        </div>
    )
}

const Nav = () => (
    <nav className="navbar">
        <SiSpacex className="space-icon" />
        <button
            onClick={() => {
                document.getElementById("launch-schedule")?.scrollIntoView({
                    behavior: "smooth",
                });
            }}
            className="launch-btn">
            LAUNCH SCHEDULE <FiArrowRight />
        </button>
    </nav>
)

const SECTION_HEIGHT = 1500;

const Hero = () => (
    <div style={{ height: `calc(${SECTION_HEIGHT}px + 100vh)` }} className="hero-div">
        <CenterImg />
        <ParallaxImgs />
        <div className="buffer-gradient" />
    </div>
)

const CenterImg = () => {

    const { scrollY } = useScroll()

    const opacity = useTransform(
        scrollY,
        [SECTION_HEIGHT, SECTION_HEIGHT + 500],
        [1, 0]
    );

    const backgroundSize = useTransform(scrollY, [0, SECTION_HEIGHT + 500], ["150%", "100%"])

    const clip1 = useTransform(scrollY, [0, SECTION_HEIGHT], [25, 0]);
    const clip2 = useTransform(scrollY, [0, SECTION_HEIGHT], [75, 100]);
    const clipPath = useMotionTemplate`polygon(${clip1}% ${clip1}%, ${clip2}% ${clip1}%, ${clip2}% ${clip2}%, ${clip1}% ${clip2}%)`
    return (
        <motion.div className="center-img-div"
            style={{
                opacity,
                backgroundSize,
                clipPath,
                backgroundImage:
                    "url(https://images.unsplash.com/photo-1460186136353-977e9d6085a1?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)",
                backgroundPosition: "center",
                backgroundRepeat: "no-repeat",
            }}
        />
    )
}

const ParallaxImgs = () => {

    return (
        <div className="parallax-imgs-div">
            <ParallaxImg
                src="https://images.unsplash.com/photo-1484600899469-230e8d1d59c0?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="And example of a space launch"
                start={-10}
                end={10}
                styles={{ width: "calc(100% / 3)" }}
            />
            <ParallaxImg
                src="https://images.unsplash.com/photo-1446776709462-d6b525c57bd3?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="An example of a space launch"
                start={30}
                end={-10}
                styles={{
                    marginLeft: "auto",
                    marginRight: "auto",
                    width: "calc(200% / 3)"
                }}
            />
            <ParallaxImg
                src="https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?q=80&w=2370&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="Orbiting satellite"
                start={-10}
                end={10}
                styles={{
                    marginLeft: "auto",
                    width: "calc(100% / 3)",
                }}
            />
            <ParallaxImg
                src="https://images.unsplash.com/photo-1494022299300-899b96e49893?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                alt="Orbiting satellite"
                start={50}
                end={-50}
                styles={{
                    marginLeft: "6rem",
                    width: "calc( 500% / 12)",
                }}
            />

        </div>
    )
}

const ParallaxImg = ({ styles, alt, src, start, end }) => {
    const ref = useRef(null)
    const { scrollYProgress } = useScroll({
        target: ref,
        offset: [`${start}vh end`, `end ${end * -1}vh`],
    })


    const opacity = useTransform(scrollYProgress, [0.75, 1], [1, 0]);
    const scale = useTransform(scrollYProgress, [0.75, 1], [1, 0.85]);

    const y = useTransform(scrollYProgress, [0, 1], [start, end]);
    const transform = useMotionTemplate`translateY(${y}vh) scale(${scale})`;
    return (
        <motion.img
            className="parallax-img"
            src={src}
            alt={alt}
            ref={ref}
            style={{
                ...styles,
                transform,
                opacity
            }}
        />
    );
}