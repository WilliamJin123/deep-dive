import { useEffect, useState } from "react";
import { useAnimate, motion, useInView } from "framer-motion";
import Reveal from "./assets/Reveal";

const imgVariants={
    initial:{scale:1, rotate:0, y:60},
    animate:{y:0, transition:{delay:0.25,duration:0.25}},
    whileHover:{scale:1.05, rotate:"3deg",  transition: {duration:0.15, ease:'easeOut'}}
}

export default function Body() {

    const [button, setButton] = useState(false);


    return (

        <div className="main">
            <div className="intro">
                <Reveal><h1>Hey, I'm William<span className="green">.</span></h1></Reveal>
                <Reveal><h3>I'm a <span className="green bold">UWaterloo Student</span></h3></Reveal>
                <Reveal><p>I have literally done 0 projects. I want to learn UI / UX Design and Animations so I can make a sick personal portfolio website
                    even though I have no projects to put on it :&#40;&#40;&#40; I want to be able to have a decent array of projects done over the next 4ish months,
                    so that I won't get completely shafted during my coop application cycle
                </p></Reveal>
                <motion.button 
                    className={button? 'button-on' : ''}
                    layout
                    initial={{
                        opacity: 0,
                        y: 75,
                    }}
                    whileInView={{ opacity: 1, y: 0, }}
                    transition={{ duration: 0.5, delay: 0.25 }}
                    viewport={{ once: true }}
                    onViewportEnter={() => setButton(true)}

                    onClick={() => document.querySelector(".contact").scrollIntoView({behavior:"smooth"})}
                >Contact me</motion.button>
                
            </div>
            <div className="about">
                <Reveal><h1>About<span className="green">.</span> <span className="break"></span></h1></Reveal>
                <div className="about-items">
                    <div className="paragraphs">
                        <Reveal><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in ligula at risus ultrices vestibulum. Nunc pharetra lectus augue, a sagittis neque hendrerit sit amet. Pellentesque magna neque, sollicitudin id ultrices nec, fringilla eu elit. Vestibulum blandit eros at ipsum.</p></Reveal>
                        <Reveal><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec feugiat nibh id egestas rutrum. Pellentesque a convallis nunc. Pellentesque ornare placerat metus, nec tempus tellus fermentum a. Nullam rhoncus, lorem vestibulum commodo placerat, tortor enim imperdiet lacus, sit amet maximu</p></Reveal>
                        <Reveal><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla in sagittis mauris. Cras blandit cursus orci nec scelerisque. Aenean vulputate urna eget elit lacinia vehicula. Curabitur dui quam, lacinia at neque id, rutrum porttitor massa. Pellentesque ac pellentesque neque, ut.</p></Reveal>
                        <Reveal> <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis ornare arcu, quis vulputate nulla feugiat quis. Sed tincidunt eget urna id hendrerit. Sed lacinia dui a egestas semper. Nulla eu quam aliquet risus congue condimentum dapibus ut dolor. Proin.
                        </p></Reveal>
                    </div>
                    <div className="lists">
                        <Reveal><div className="list-grid">
                            <h4> <i className="fa-solid fa-briefcase"></i>Use for work</h4>
                            <span className="chip">TypeScript</span>
                            <span className="chip">JavaScript</span>
                            <span className="chip">HTML</span>
                            <span className="chip">CSS</span>
                            <span className="chip">React</span>
                            <span className="chip">Redux</span>
                            <span className="chip">NodeJS</span>
                            <span className="chip">Express</span>
                            <span className="chip">Postgres</span>
                            <span className="chip">MongoDB</span>
                            <span className="chip">GitHub</span>
                            <span className="chip">Jira</span>
                            <span className="chip">Heroku</span>
                            <span className="chip">AWS</span>
                        </div>
                        </Reveal>
                        <Reveal>
                            <div className="list-grid">
                                <h4> <i className="fa-solid fa-gamepad"></i>Use for fun</h4>
                                <span className="chip">Rust</span>
                                <span className="chip">Tailwind</span>
                                <span className="chip">Java</span>
                                <span className="chip">Spring</span>
                                <span className="chip">Figma</span>
                                <span className="chip">Whimsical</span>
                                <span className="chip">Planetscale</span>
                                <span className="chip">GraphQL</span>
                                <span className="chip">Python</span>
                                <span className="chip">FastAPI</span>
                            </div>
                        </Reveal>
                    </div>

                </div>
                <Reveal>
                    <div className="links">
                        <div className="green">My Links: </div>
                        <a href="https://github.com/WilliamJin123?tab=repositories"><i className="fa-brands fa-linkedin"></i></a>
                        <a href="https://github.com/WilliamJin123?tab=repositories"><i className="fa-brands fa-github"></i></a>
                        <a href="https://github.com/WilliamJin123?tab=repositories"><i className="fa-brands fa-square-youtube"></i></a>

                    </div>
                </Reveal>
            </div>
            <div className="projects">
                <Reveal><h1><div className="break"></div> Projects<span className="green">.</span></h1></Reveal>

                <div className="projects-grid">

                    <div className="project">
                        <motion.div className="img"
                        initial={{y:100}}
                        whileInView={{y:0, transition:{delay:0.25,duration:0.5}}}
                        viewport={{once:true}}
                        ><motion.img src={`https://picsum.photos/1000/1000?random=${Math.random()}`}
                            variants={imgVariants}
                            initial="initial"
                            animate="animate"
                            whileHover="whileHover"
                        ></motion.img></motion.div>
                        <Reveal><h3>Project X1</h3></Reveal>
                        <Reveal><div>
                            <div className="green project-lang">Flutter - MUI - Python - FastAPI</div>
                            A real-time coaching app for students learning to paint. This app is my baby, designed and built on my own.
                            <a href="#">Learn more <span>&gt;</span></a>
                        </div></Reveal>

                    </div>
                    <div className="project">
                        <motion.div className="img"
                        initial={{y:100}}
                        whileInView={{y:0, transition:{delay:0.25,duration:0.5}}}
                        viewport={{once:true}}
                        ><motion.img src={`https://picsum.photos/1000/1000?random=${Math.random()}`}
                        variants={imgVariants}
                        initial="initial"
                        animate="animate"
                        whileHover="whileHover"
                        ></motion.img></motion.div>


                        <Reveal><h3>Project X</h3></Reveal>
                        <Reveal><div>
                            <div className="green project-lang">Flutter - MUI - Python - FastAPI</div>
                            A real-time coaching app for students learning to paint. This app is my baby, designed and built on my own.
                            <a href="#">Learn more <span>&gt;</span></a>
                        </div></Reveal>

                    </div>
                    <div className="project">
                        <motion.div className="img"
                        initial={{y:100}}
                        whileInView={{y:0, transition:{delay:0.25,duration:0.5}}}
                        viewport={{once:true}}
                        ><motion.img src={`https://picsum.photos/1000/1000?random=${Math.random()}`}
                        variants={imgVariants}
                        initial="initial"
                        animate="animate"
                        whileHover="whileHover"
                        ></motion.img></motion.div>


                        <Reveal><h3>Project X</h3></Reveal>
                        <Reveal><div>
                            <div className="green project-lang">Flutter - MUI - Python - FastAPI</div>
                            A real-time coaching app for students learning to paint. This app is my baby, designed and built on my own.
                            <a href="#">Learn more <span>&gt;</span></a>
                        </div></Reveal>

                    </div>
                    <div className="project">
                        <motion.div className="img"
                        initial={{y:100}}
                        whileInView={{y:0, transition:{delay:0.25,duration:0.5}}}
                        viewport={{once:true}}
                        ><motion.img src={`https://picsum.photos/1000/1000?random=${Math.random()}`}
                        variants={imgVariants}
                        initial="initial"
                        animate="animate"
                        whileHover="whileHover"
                        ></motion.img></motion.div>

                        <Reveal> <h3>Project X</h3></Reveal>
                        <Reveal><div>
                            <div className="green project-lang">Flutter - MUI - Python - FastAPI</div>
                            A real-time coaching app for students learning to paint. This app is my baby, designed and built on my own.
                            <a href="#">Learn more <span>&gt;</span></a>
                        </div></Reveal>

                    </div>
                </div>
            </div>
            <div className="contact">
                <Reveal><h1>Contact<span className="green">.</span></h1></Reveal>
                <Reveal><p>Shoot me an email if you want to connect! You can also find me on Linkedin or Twitter if that's more your speed.</p></Reveal>

                <div className="contact-email">
                    <Reveal><a href="#"><i className="fa-solid fa-envelope"></i> jinwilliam.jin@gmail.com</a></Reveal>
                    <br/>
                    <Reveal><a href="https://steam-portfolio-demo.vercel.app/">This website was based on: https://steam-portfolio-demo.vercel.app/</a></Reveal>
                </div>
            </div>
        </div>
    )
}