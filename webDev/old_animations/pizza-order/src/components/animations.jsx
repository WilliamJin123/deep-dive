

export const defaultVariant={
    transition:{
        type:'spring',
        stiffness:50,
        delay:0
    }
}
export const childVariant = {
    initial: {
        opacity:0
    },
    animation:{
        opacity:1,
        transition:{
            duration:1,
            staggerChildren:0.4
        }
    }
}

export const pageVariant ={
    initial: {
        opacity: 0,
        x:'100vw'
    },
    animation: {
        x:0,
        opacity:1,
        transition:{
            type:'spring',
            stiffness:50,
            delay:0,
            mass:0.4,
            damping: 8,
            when:'beforeChildren',
            staggerChildren:0.4,
        }
    },
}


export const listItemVariant ={
    
    whileHover:{
        scale:1.3,
        color:'#f8e112',
        originX:0
    },
    initial:{
        x:'100vw'
    },
    animation:{
        x:0,
        
    },
    // transition:{
        // type:'spring',
        // stiffness:50,
        // delay:0,
        // mass:0.4,
        // damping: 8,
        // staggerChildren:0.4,
    // }
   
}
export const buttonVariant = {
    initial: {
        opacity: 0,
        scale: 0.1,
        backgroundColor: 'transparent', // or whatever your default color is
        color: 'var(--white)', // Default text color
    },
    whileHover:{
        // scale:[1.25,1.35,1.25],
        scale:1.15,
        y:-5,
        backgroundColor:'var(--white)',
        color:'#58066F',
        boxShadow: '0px 0px 4px rgb(255,255,255)',
        transition:{
            duration: 0.3,
            ease:'easeInOut',
            scale:{
                repeat:Infinity, 
                repeatType:'reverse',
                // times:[0,0.5,1],
                duration:0.6,
                delay:1,
            }
           
        }
    },
    whileTap:{
        scale:1.2,
        transition:{
            duration: 0.3,
            ease:'easeInOut',
        }
    }
}
export const homePageVariant ={
    visible: {
        
        opacity:0.7,
        scale:1,
        transition:{
            duration:1,
            ease: [0.2, 0.79, 0.59, 0.95],
            delay:0.1,
            
        },
        

    }
}

export const containerVariant = {
    hidden:{
        opacity:0.3,
        color:'var(--red)',
        rotateY:180,
    },
    visible:{
        scale:1,
        color:'var(--white)',
        opacity: 1,
        rotateY:0,
        transition:{
            duration:1,
            ease: [0.2, 0.79, 0.59, 0.95],
            delay:0.2,
        },
        when:'beforeChildren'
    },
    exit: {
        x:'-100vw',
        opacity:0,
        transition:{
            duration:0.5,
            ease: 'easeOut'
        },
        when:'afterChildren',
    }
}

export const backdropVariant = {
    visible:{
        opacity: 1,
        transition:{
            duration:1
        }
    },
    hidden:{
        opacity:0,
    }
}

export const svgVariant = {
    initial: {rotate: -180},
    animate:{
        rotate:0,
        transition:{
            duration:1,

        }
    }
}
export const pathVariant = {
    initial:{
        opacity:0,
        pathLength: 0, //draws it
    },
    animate:{
        opacity:1,
        pathLength:1,
        transition:{
            duration:2,
            ease:"easeInOut"
        }
    }
}

export const loaderVariant = {
    animationOne:{
        x:[-20, 20],
        y:[0, -30],
        transition:{
            x:{repeat:Infinity,
                repeatType:'reverse', 
                duration:0.5},
            y:{repeat:Infinity,
                repeatType:'reverse',
                duration:0.25,
                ease:'easeOut'},
        }
    },
    animationTwo:{
        y:[0,-40],
        x:0,
        transition:{
            y:{
                repeat:Infinity,
                repeatType:'reverse',
                ease:'easeOut',
                duration:0.25
            }
        }
    }
}