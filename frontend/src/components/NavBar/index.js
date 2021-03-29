import React from 'react'
import {
  Link,
} from "react-router-dom"

import { Links, NavItem, NavbarContainer, NavbarInner, Brand } from './styles'

const Navbar = () => {
    return (
      <NavbarContainer>
          <NavbarInner>
            <Link to='/' style={{textDecoration: 'none'}}> <Brand>SumRisk</Brand></Link>
                  <Links>
                      <Link to='/'><NavItem>home</NavItem></Link>
                      <Link to='/about'><NavItem>about</NavItem></Link>
                  </Links>
              </NavbarInner>
      </NavbarContainer>

    )
}

export default Navbar
