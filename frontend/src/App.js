import React from 'react'
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'
import axios from 'axios'
import AuthorList from './components/Authors.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBooks.js';
import LoginForm from './components/LoginForm.js';
import BookForm from './components/BookForm.js';

const NotFound = ({location}) => {
    return (<div>Page not found: {location.pathname}</div>)
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }

    getToken(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
        .then(response => {
            console.log(response.data.token)
            localStorage.setItem('token', response.data.token)
            this.setState({'token': response.data.token}, this.loadData)
        })
        .catch(error => alert("Wrong password"))
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({'token': ''}, this.loadData)
    }

    isAuthenticated() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuthenticated()) {
            return {'Authorization': 'Token ' + this.state.token}
        }
        return {}
    }

    createBook(title, authors) {
        const headers = this.getHeaders()
        axios.post('http://127.0.0.1:8000/api/books/', {'title': title, 'authors': authors} , {headers})
        .then(response => {
            this.loadData();
        })
        .catch(error => {
            console.log(error)
        })
    }

    deleteBook(id) {
        const headers = this.getHeaders()
        axios.delete(`http://127.0.0.1:8000/api/books/${id}/`, {headers})
        .then(response => {
            this.setState( {
                'books': this.state.books.filter((book) => book.id != id)
            })
        })
        .catch(error => {
            console.log(error)
        })
    }

    loadData() {
        const headers = this.getHeaders()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
        .then(response => {
            const authors = response.data
            this.setState( {
                'authors': authors
            })
        })
        .catch(error => {
            console.log(error)
            this.setState({
                'authors': []
            })
        })
        axios.get('http://127.0.0.1:8000/api/books/', {headers})
        .then(response => {
            const books = response.data
            this.setState( {
                'books': books
            })
        })
        .catch(error => {
            console.log(error)
            this.setState({
                'books': []
            })
        })
    }

    componentDidMount() {
        const token = localStorage.getItem('token')
        console.log(token)
        this.setState({'token': token}, this.loadData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Authors</Link></li>
                            <li><Link to='/books'>Books</Link></li>
                            <li><Link to='/books/create'>Create book</Link></li>
                            <li>
                                { this.isAuthenticated() ?
                                    <button onClick={()=>this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>
                                }
                            </li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route path='/' exact component={() => <AuthorList authors = {this.state.authors}/>} />
                        <Route path='/books' exact component={() => <BookList books = {this.state.books} deleteBook={(id) => this.deleteBook(id)}/>} />
                        <Route path='/books/create' exact component={() => <BookForm authors = {this.state.authors} createBook={(title, authors) => this.createBook(title, authors)}/>} />
                        <Route path='/login' exact component={() => <LoginForm getToken={(login, password) => this.getToken(login, password)} />} />
                        <Route path='/author/:id' component={() => <AuthorBookList books = {this.state.books}/>} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
