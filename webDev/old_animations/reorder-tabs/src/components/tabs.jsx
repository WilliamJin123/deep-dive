import {Reorder, motion} from "framer-motion"

export default function Tab({item, handleDelete, handleSelect, isSelected}) {

    return(
        <Reorder.Item value={item} 
            className="tab"
            onPointerDown={handleSelect}
            initial={{y: 50, opacity: 0}}
            animate={{y: 0, opacity: 1, backgroundColor: isSelected ? "var(--gray)" : "var(--white)",
                transition: {duration: 0.15}
            }}
            exit={{opacity: 0, y: 20, transition:{duration:0.3} }}
        >
            <motion.div layout="position" className="fade" whileDrag={{ backgroundColor: "var(--dark-gray)"}}> <span >{item.icon}{item.label}</span>
            </motion.div>
            <motion.button className="delete" layout
                initial={false}
                animate={{ backgroundColor: isSelected ? "var(--dark-gray)" : "var(--white)"}}
                onPointerDown={(event) => {
                    event.stopPropagation();
                    handleDelete();
                  }}
            > <span>+</span> </motion.button>
        </Reorder.Item>
    )
}