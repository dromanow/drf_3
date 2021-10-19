import React from 'react'

const BookItem = ({book, deleteBook}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.title}</td>
            <td>{book.authors}</td>
            <td><button type='button' onClick={()=>deleteBook(book.id)}>Delete</button></td>
        </tr>
    )
} 


const BookList = ({books, deleteBook}) => {
    return (
        <table>
            <th>id</th>
            <th>title</th>
            <th>authors</th>
            {books.map((b) => <BookItem book={b} deleteBook={deleteBook}/>)}
        </table>
    )
}

export default BookList
