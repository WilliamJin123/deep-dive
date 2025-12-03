import { useState } from 'react'
import { Reorder } from 'framer-motion';
import './App.css'
const initialItems = ["🍅 Tomato", "🥒 Cucumber", "🧀 Cheese", "🥬 Lettuce"];

function App() {
  console.log('loaded')
  const [items, setItems] = useState(initialItems)
  return(
    <Reorder.Group axis="y" values = {items} onReorder={setItems} className='item-list'>
      {items.map(item => (
        <Reorder.Item key={item} value={item} className="item">
          {item}
        </Reorder.Item>
      ))}
    </Reorder.Group>
  )
}

export default App
