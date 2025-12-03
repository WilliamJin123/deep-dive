

export const svgVariants = {
    open:{
        rotate:180
    },
    closed:{
        rotate:0
    },
    transition:{
        duration:0.1,
        ease:"easeInOut"
        
    }
}

export const buttonVariants={
    whileTap:{
        scale:0.95
    }
}

export const listVariants={
    open:{
        scale:1,
        clipPath: "inset(0% 0% 0% 0% round 15px)",
        transition: {
            type: "spring",
            bounce: 0,
            duration: 0.7,
            when:"beforeChildren",
            // staggerChildren: 0.07
          },
    },
    closed:{
        clipPath: "inset(10% 50% 90% 50% round 15px)",
        transition: {
            type: "spring",
            bounce: 0,
            duration: 0.3
          }
    },
   
}
export const itemVariants={
    closed:{
        opacity:0,
        y:30,
        
    },
    open: i =>({
        scale:1,
        opacity:1,
        y:0,
        transition:{
            duration:0.5,
            type:"spring",
            bounce: 0.5,
            stiffness:200,
            delay: i%2=== 0? i*0.07 : 0.5 + i*0.07
        }
    })
}