import React from 'react'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
} 


const BookList = ({books}) => {
    return (
        <table>
            <th>id</th>
            <th>title</th>
            <th>authors</th>
            {books.map((b) => <BookItem book={b} />)}
        </table>
    )
}

export default BookList
