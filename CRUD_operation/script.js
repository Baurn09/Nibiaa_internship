import express from "express";
import {open} from "sqlite"
import sqlite3 from "sqlite3"

const app = express()
const PORT = 3000;

app.use(express.json())

const db = await open({
    filename: "./database.db", 
    driver: sqlite3.Database
})

console.log("Connect to Database")

await db.exec(`
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL
    )   
`)

//to post the item
app.post("/items", async (req, res)=>{
    try {
        const {name} = req.body;

        if (name == ""){
            return res.status(404).json({message: "name not found"})
        }

       const result = await db.run("INSERT INTO items(name) VALUES (?)", [name])

        res.status(201).json({
            id: result.lastID, 
            name
        })
    } catch (error) {
        res.status(500).json(error)
    }
})

//to get all the items
app.get("/items", async (req, res)=>{
    const items = await db.all("SELECT * FROM items")
    res.json(items)
})

//to get single item
app.get("/items/:id", async (req, res)=>{
    const id = Number(req.params.id)

    const item = await db.get("SELECT * FROM items WHERE id = ?", [id])
    if(!item){
        return res.status(404).json({message : "items not found"})
    }

    res.json({message: "single item parse successfully", item: item})

})

//to update an item 
app.put("/items/:id", async (req, res)=>{
    const id = Number(req.params.id)
    const {name} = req.body

    const result = await db.run("UPDATE items SET name = ? WHERE id = ?", [name, id])

    if(result.changes === 0){
        return res.status(404).json({message : "items not found"})
    }
    const updated_item = await db.get("SELECT * FROM items WHERE id = ?", [id])

    res.json({meessage: "item updated successfully", result: updated_item})
})

//to delete
app.delete("/items/:id", async (req, res)=>{
    const id = Number(req.params.id)
    
    const result = await db.run("DELETE FROM items WHERE id = ?", [id])

    if(result.changes === 0 ){
        return res.status(404).json({message : "items not found"})
    }
    // await db.run("DELETE FROM items");
    // await db.run("DELETE FROM sqlite_sequence WHERE name = 'items'");

    res.json({
        message: "Item deleted successfully"
    });

})


app.listen(PORT, ()=>{
    console.log(`Server is listen on port ${PORT}`)
})