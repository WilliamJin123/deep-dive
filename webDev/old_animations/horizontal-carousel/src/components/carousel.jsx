import { useState, useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import "./carousel.css"

export default function Carousel() {
    const carouselRef = useRef(null)
    const { scrollYProgress } = useScroll({ target: carouselRef });
    const x = useTransform(scrollYProgress, [0, 1], ['0%', '-95%'])

    const images = []
    for (let i = 0; i < 10; i++) {
        images.push(`https://picsum.photos/1000/1000?random=${Math.random()}`)
    }
    const imagesMap = images.map((image, index) => (
        <li key={index}><img className="carousel-img" src={image}></img></li>

    ))
    return (
        <section className="carousel-section" ref={carouselRef}>
            <div className="carousel-div">
                <motion.ul className="carousel"
                    style={{ x }}
                >{imagesMap}</motion.ul>
            </div>
        </section>


    )
}
