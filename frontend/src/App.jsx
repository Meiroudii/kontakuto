import { useState, useEffect } from 'react'
import './App.css'
import ContactList from './ContactList'
import ContactForm from './ContactForm'

function App() {
    // On contacts backend fetching!
    // TODO: create for [backlist, speciallist, real friendlist]
    const [contacts, setContacts] = useState([])

    // NOTE: useEffect when renders it will call the fetchContacts() and set it on useState
    useEffect(() => {
        fetchContacts()
    }, [])
    const fetchContacts = async () => {
        const response = await fetch("http://127.0.0.1:5000/contacts")
        const data = await response.json()
        setContacts(data.contacts)
        console.log(data.contacts)
    }
  return <>
            <ContactList contacts={contacts} />
            <ContactForm />
        </>}

export default App;
