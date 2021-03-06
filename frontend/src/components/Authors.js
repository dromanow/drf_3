import React from 'react'
import {Link} from 'react-router-dom'


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>{author.first_name}</td>  
            <td><Link to={`author/${author.id}`} >{author.last_name}</Link> </td>
            <td>{author.birthday_year}</td>  
        </tr>
    )
} 


const AuthorList = ({authors}) => {
    return (
        <table>
            <th>first_name</th>
            <th>last_name</th>
            <th>birthday_year</th>
            {authors.map((a) => <AuthorItem author={a} />)}
        </table>
    )
}

export default AuthorList
