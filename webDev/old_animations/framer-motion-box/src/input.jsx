
export default function Input({onChange, min = -600, max = 600, value, children}){

    return(
        <label>
            <code>{children}</code>
            <input
                className="slider"
                type="range"
                value = {value}
                onChange={e => onChange(parseFloat(e.target.value))}
                min = {min}
                max = {max}
            ></input>
            <input
                type="text"
                value = {value}
                onChange={e => onChange(parseFloat(e.target.value)) || 0}
                min = {min}
                max = {max}
            ></input>
        </label>
    )
}