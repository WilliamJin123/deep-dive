import { useState, useRef, useEffect} from 'react'
import {motion, useMotionValue, useSpring, useTransform, } from "framer-motion";
import {FiArrowRight} from "react-icons/fi"
import './HoverLinks.css'

const links = [
  {
    heading: "About",
    subheading: "Learn what we do here",
    imgSrc: `https://picsum.photos/300/250?random=${Math.random()}`,
    href: "#",
  },
  {
    heading: "Clients",
    subheading: "We work with great people",
    imgSrc: `https://picsum.photos/300/250?random=${Math.random()}`,
    href: "#",
  },
  {
    heading: "Portfolio",
    subheading: "Our work speaks for itself",
    imgSrc: `https://picsum.photos/300/250?random=${Math.random()}`,
    href: "#",
  },
  {
    heading: "Careers",
    subheading: "We want cool people",
    imgSrc: `https://picsum.photos/300/250?random=${Math.random()}`,
    href: "#",
  },
  {
    heading: "Fun",
    subheading: "Incase you're bored",
    imgSrc: `https://picsum.photos/300/250?random=${Math.random()}`,
    href: "#",
  },
];


export default function HoverLinks() {

  return (
    <section className='hover-section'>
        <div className='hover-div'>
            {links.map((link, index) => (
                <Link 
                    key={index}
                    heading = {link.heading}
                    subheading={link.subheading}
                    imgSrc={link.imgSrc}
                    href={link.href}
                />
            ))}
        </div>
    </section>
  )
}


function Link({heading, subheading, imgSrc, href}) {

    const aRef = useRef(null)
    const [aRect, setARect] = useState(null);

    const x = useMotionValue(0)
    const y = useMotionValue(0)

    const springX = useSpring(x);
    const springY = useSpring(y);
    const top = useTransform(springX, [0.5, -0.5], ['40%', '60%'])
    const left = useTransform(springY, [0.5, -0.5], ['60%', '70%'])


    useEffect(() => {
      const updateRect = () => {
        
        const rect = aRef.current.getBoundingClientRect();
        setARect(rect)
        console.log(rect)
      }
      updateRect()
      window.addEventListener('resize', updateRect)

      return () => window.removeEventListener('resize', updateRect)
    }, [])
    function handleMouseMove(event) {
      const width = aRect.width
      const height = aRect.height

      const mouseX = event.clientX - aRect.left
      const mouseY = event.clientY - aRect.top
      
      const xPct = mouseX / width - 0.5
      const yPct = mouseY / height - 0.5
      x.set(xPct)
      y.set(yPct)
      
    }
    return(
        <motion.a href={href} ref={aRef} className='hover-link'
          onMouseMove={handleMouseMove}
          initial = "initial"
          whileHover="whileHover"
        >
          <div>
            <motion.h1
              variants={{
                initial:{x:0,},
                whileHover:{x:-16,}
              }}
              transition={{type:'spring',}}
            >
              {heading.split("").map((letter, index) => (
              <motion.span key={index}
                variants={{
                  initial:{x:0,},
                  whileHover:{x:16, transition:{type:'spring', delay:0.25 + index*0.075}}
                }}
                transition={{type:'spring'}}
              >
                {letter}
              </motion.span>
            ))}
            
            </motion.h1>
            <div className='subheading'>{subheading}</div>
          </div>
          
          <motion.img src={imgSrc} alt={`Image representing ${heading} link`}
            className='hover-link-img'
            layout
            style={{
              top,
              left,
              translateX: '-50%',
              translateY: '-50%',
            }}
            variants={{
              initial: { scale: 0, rotate: "-12.5deg" },
              whileHover: { scale: 1, rotate: "12.5deg" },
            }}
            transition={{ type: "spring" }}
          />

          <motion.div className='arrow'
            variants={{
              initial: {
                x: "25%",
                opacity: 0,
              },
              whileHover: {
                x: "0%",
                opacity: 1,
              },
            }}
            transition={{type:'spring'}}
          >
            <FiArrowRight/>
          </motion.div>

        </motion.a>
    )
}

