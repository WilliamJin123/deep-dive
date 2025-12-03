import {useRef, useState} from "react";
import { motion, AnimatePresence, useScroll, } from "framer-motion";
import { Link, useLocation } from "react-router-dom";

export default function Header({}){
    const location = useLocation();
    const currentPath = location.pathname;
    return(
        <div className="header">
            <Link to="/" style={{opacity: currentPath === "/" ? 1 : 0.5 }} className="link"> Images</Link>
            <Link to="/about" style={{opacity: currentPath === "/about" ? 1 : 0.5 }} className="link"> About </Link>
        </div>
    )
}