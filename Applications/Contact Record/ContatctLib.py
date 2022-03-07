from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E, N, S, Entry, END, StringVar, Scrollbar, Toplevel
from tkinter import ttk
import re
import mysql.connector as mc


regex = re.compile( r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' )


class Contacts:

    def __init__(self, root):
        self.connection = mc.connect( host="localhost", user="root", password="2323", database="contacts" )
        self.root = root
        self.create_gui()
        self.name = " "
        ttk.style = ttk.Style()
        ttk.style.configure( "Treeview", font=('helvetica', 10) )
        ttk.style.configure( "Treeview.Heading", font=('helvetica', 12, 'bold') )

    def create_gui(self):
        self.create_left_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_scrollbar()
        self.create_bottom_buttons()
        self.get_contacts()

    def create_left_icon(self):
        photo = PhotoImage( file='contLogo.gif' )
        label = Label( image=photo )
        label.image = photo
        label.grid( row=0, column=0 )

    def create_label_frame(self):
        labelframe = LabelFrame( self.root, text='Create New Contact', bg="sky blue", font="helvetica 10" )
        labelframe.grid( row=0, column=1, padx=8, pady=8, sticky='ew' )
        Label( labelframe, text='Name:', bg="green", fg="white" ).grid( row=1, column=1, sticky=W, pady=2, padx=15 )
        self.namefield = Entry( labelframe )
        self.namefield.grid( row=1, column=2, sticky=W, padx=5, pady=2 )
        Label( labelframe, text='Email:', bg="brown", fg="white" ).grid( row=2, column=1, sticky=W, pady=2, padx=15 )
        self.emailfield = Entry( labelframe )
        self.emailfield.grid( row=2, column=2, sticky=W, padx=5, pady=2 )
        Label( labelframe, text='Number:', bg="black", fg="white" ).grid( row=3, column=1, sticky=W, pady=2, padx=15 )
        self.numfield = Entry( labelframe )
        self.numfield.grid( row=3, column=2, sticky=W, padx=5, pady=2 )
        Button( labelframe, text='Add Contact', command=self.add_new_contact, bg="blue",
                fg="white" ).grid( row=4, column=2, sticky=E, padx=5, pady=5 )

    def create_message_area(self):
        self.message = Label( text='', fg='red' )
        self.message.grid( row=3, column=1, sticky=W )

    def create_tree_view(self):
        self.tree = ttk.Treeview( height=10, columns=("email", "number"), style='Treeview' )
        self.tree.grid( row=6, column=0, columnspan=3 )
        self.tree.heading( '#0', text='Name', anchor=W )
        self.tree.heading( "email", text='Email Address', anchor=W )
        self.tree.heading( "number", text='Contact Number', anchor=W )

    def create_scrollbar(self):
        self.scrollbar = Scrollbar( orient='vertical', command=self.tree.yview )
        self.scrollbar.grid( row=6, column=3, rowspan=10, sticky='sn' )

    def create_bottom_buttons(self):
        Button( text='Delete Selected', command=self.delete_contact, bg="red", fg="white" ).grid( row=8, column=0, sticky=W, pady=10,
                                                                                 padx=20 )
        Button( text='Modify Selected', command=self.on_modify_selected_button_clicked, bg="purple", fg="white" ).grid( row=8, column=1, sticky=W )

    def run_query(self, query, command):
        result = str()
        if command == "GET":
            cursor = self.connection.cursor()
            cursor.execute( query )
            result = cursor.fetchall()
            cursor.execute( "commit" )
        if command == "INSERT":
            cursor = self.connection.cursor()
            cursor.execute( query )
            cursor.execute( "commit" )
        if command == "DELETE":
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.execute("commit")
        if command == "UPDATE":
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.execute("commit")
        return result

    def get_contacts(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete( element )
        # Obtaining Data
        query1 = 'SELECT * FROM contacts.contact_book ORDER BY name desc'
        rows1 = self.run_query( query1, "GET" )
        for row in rows1:
            self.tree.insert( '', 0, text=row[1], values=(row[2], row[3]) )

    @property
    def new_contacts_validated(self):
        if len( self.namefield.get() ) == 0:
            return False
        elif len( self.emailfield.get() ) != 0 and not (re.fullmatch( regex, self.emailfield.get() )):
            return False
        elif len(self.numfield.get()) != 10:
            return False
        return True

    def add_new_contact(self):
        if self.new_contacts_validated:
            pname = self.namefield.get()
            pemail = self.emailfield.get()
            pnum = self.numfield.get()
            query = "INSERT INTO contacts.contact_book(name,mobile,email) VALUES('" + pname + "','" + pnum + "','" + pemail + "')"
            self.run_query( query, "INSERT" )
            self.message['text'] = f'New Contact {pname} added'
            self.namefield.delete( 0, END )
            self.emailfield.delete( 0, END )
            self.numfield.delete( 0, END )

        else:
            self.message['text'] = 'name,email and number cannot be blank'

        self.get_contacts()

    def delete_contact(self):
        self.message['text'] = ""
        try:
            self.tree.item( self.tree.selection() )['text']
        except IndexError as e:
            self.message['text'] = "Please select a Record"
            return
        self.message['text'] = ""

        pname = self.tree.item( self.tree.selection() )['text']

        query = "DELETE FROM contacts.contact_book WHERE name='{}'".format( pname )
        self.run_query( query, "DELETE" )
        self.message['text'] = "Contact {} deleted successfully".format( pname )

        # Filling the GUI
        self.get_contacts()

    def on_modify_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            self.tree.item( self.tree.selection() )['values'][0]

        except IndexError as e:
            self.message['text'] = 'No item selected to modify'
            return
        self.open_modify_window()

    def open_modify_window(self):
        name = self.tree.item( self.tree.selection() )['text']
        old_number = self.tree.item( self.tree.selection() )['values'][1]
        self.transient = Toplevel()
        self.transient.title( 'Update Contact' )
        Label( self.transient, text='Name:' ).grid( row=0, column=1 )
        Entry( self.transient, textvariable=StringVar(
            self.transient, value=name ), state='readonly' ).grid( row=0, column=2 )
        Label( self.transient, text='Old Contact Number:' ).grid( row=1, column=1 )
        Entry( self.transient, textvariable=StringVar(
            self.transient, value=old_number ), state='readonly' ).grid( row=1, column=2 )

        Label( self.transient, text='New Phone Number:' ).grid(
            row=2, column=1 )
        new_phone_number_entry_widget = Entry( self.transient )
        new_phone_number_entry_widget.grid( row=2, column=2 )

        Button( self.transient, text='Update Contact', command=lambda: self.edit_contacts(
            new_phone_number_entry_widget.get(), name ) ).grid( row=3, column=2, sticky=E )

        self.transient.mainloop()

    def edit_contacts(self, newphone, name):
        try:
            query = "UPDATE contacts.contact_book SET mobile='{}' WHERE name='{}'".format(
                newphone, name )
            self.run_query(query, "UPDATE" )
            self.transient.destroy()
            self.message['text'] = "Contact {} Updated Successfully".format( name )

        except Exception as e:
            print( e )
            self.message['text'] = "Error in updating Name {}".format( name )

        # Filling the GUI
        self.get_contacts()


if __name__ == '__main__':
    mw = Tk()
    application = Contacts( mw )
    mw.title( "Contacts" )
    mw.mainloop()
