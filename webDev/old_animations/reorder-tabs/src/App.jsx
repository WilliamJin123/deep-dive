import "./App.css"
import { Reorder, AnimatePresence, motion } from "framer-motion"
import { initialTabs, allIngredients, getNextIngredient } from "./components/ingredients"
import { useState, useRef } from "react"
import Tab from "./components/tabs"
export default function App() {
  const [tabs, setTabs] = useState(initialTabs)
  const [selected, setSelected] = useState(tabs[0])

  function add(){
    const next = getNextIngredient(tabs)
    if (next){
      setTabs(prev => [
        ...prev,
        next
      ])
      setSelected(next)
    }
  }
  const newIndex = useRef(0)
  function remove(item) {
    const index = tabs.indexOf(selected)
    if (item === selected){
      
      
      if (index === -1){
        newIndex.current = 0
      } else if (index === tabs.length - 1){
        newIndex.current = tabs.length - 2
      }else{
        newIndex.current = index + 1
      }
      setSelected(tabs[newIndex.current])
    }
    setTabs(prev => {
      const updatedTabs = [...prev]
      updatedTabs.splice(index, 1)
      return updatedTabs
    }
    )
  }
  return (
    <div className="main">
      <div className="tabs-area">
        <Reorder.Group className="tabs"
          axis="x" onReorder={setTabs} layoutScroll
          values={tabs}
          
        >
          <AnimatePresence initial={false}>
            {tabs.map(item => (
              <Tab key = {item.label} item={item} isSelected={selected===item} handleSelect={() => setSelected(item)} handleDelete={() => remove(item)} />
            ))}
          </AnimatePresence>
        </Reorder.Group>
        
      </div>
      <motion.button className="add" disabled={tabs.length === allIngredients.length}
          onClick={add}
          whileTap={{scale: 0.9}}
        >
          +
        </motion.button>

      <AnimatePresence mode="wait"
      >
        <div className="main-display">
        <motion.div 
        key={selected ? selected.label : "none"}
        initial={{y: 20, opacity: 0}}
        animate ={{y: 0, opacity: 1}}
        exit= {{y: -20, opacity: 0}}
        transition={{ duration: 0.2 }}
        >
            {selected ? selected.icon : "😋"}
        </motion.div>
        </div>
      </AnimatePresence>
    </div>

  )
}