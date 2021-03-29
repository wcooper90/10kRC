import styled from 'styled-components'

export const NavbarContainer = styled.div`
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: center;
`

export const NavbarInner = styled.div`
    width: 100%;
    max-width: 1024px;
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: space-between;
`

export const Brand = styled.h2`
  border-bottom: 2px solid black;
  text-decoration: none;
  color: #008080;
`

export const Hamburger = styled.div`
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
  display: block;
  height: 30px;
  transform: ${(props) => (props.slide ? "translateX(-40vw)" : null)};
`;

export const Bar = styled.p`
  border-radius: 25px;
  height: 3px;
  background-color: #8A4F7D;
  margin: 6px 0;
  transition: all 0.7s cubic-bezier(0.25, 0.8, 0.25, 1);
  width: ${(props) => 35 - props.num * 7 + "px"};

  /* width: 30px;  */
  `;

  export const Button = styled.button`
    padding: 8px 20px;
    border-radius: 4px;
    background-color: #8A4F7D;
    margin-left: 20px;
    border: none;
    color: #8A4F7D;
    font-size: 16px;
    box-shadow: 0 2px 0 rgba(0,0,0,.045);
    height: 40px;
    font-weight: 600;
  `


  export const NavItem = styled.p`
  font-size: 16px;
  position: relative;
  margin: 0px;
  margin-left: 20px;
  margin-right: 20px;
  transition: 0.2s;
  width: fit-content;
  border-bottom: 2px solid black;
  text-align: center;

  &:hover {
      border-bottom: 2px solid #8A4F7D;
      cursor: pointer;

  }

  &:hover a {
    color: rgba(31, 45, 61, 1);
  }
`;

export const Links = styled.div`
    justify-content: center;
    display: flex;
    align-items: center;


  & a {
    color: rgba(31, 45, 61, 0.5);
    font-size: 1.2rem;
    text-decoration: none;
    transition: 0.2s;
    font-weight: 600;
  }

  & a:visited {
    color: black;
  }
`;
