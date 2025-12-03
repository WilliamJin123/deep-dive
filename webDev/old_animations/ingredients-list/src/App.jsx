import { useState } from 'react';
import './App.css';
import { tabs } from './Ingredients';
import { AnimatePresence, motion } from 'framer-motion';


function App() {
  const [selected, setSelected] = useState(tabs[0])
  const tabList = tabs.map((tab, index) => (
    <li key={index} className={tab === selected ? 'selected' : ''}
      onClick={() => setSelected(tabs[index])}
    >
      <span>{tab.icon}</span>
      <span>{tab.label}</span>
      {tab === selected && (
        <motion.div className='underline' layoutId='underline'
          transition={{type:'spring', stiffness:200, damping:15, mass:0.5 }}
        />
      )}
    </li>
  ))
  return (
    <div className="main">
      <ul className='ingred-list'>
        {tabList}
      </ul>
      <AnimatePresence mode="wait">
        <motion.div className='display'
          key={selected.label}
          initial={{y:10, opacity: 0}}
          animate={{y:0, opacity:1}}
          exit={{y:-10, opacity:0}}
          transition={{ duration: 0.2 }}
        >
          {selected.icon}
        </motion.div>
      </AnimatePresence>

    </div>
  );
}

export default App;