import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime

# Streamlit App Title
st.set_page_config(
    page_title="Local Food Waste Management", 
    layout="wide",
    page_icon= "🥗"
    )

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Information", "Crud Operations", "Queries","Learner Queries","Contact","Feedback","Creator"])

connection = sqlite3.connect("food_waste_management.db")
cursor = connection.cursor()

def read_provider():
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor() 
    c.execute('SELECT * FROM providers')
    data = c.fetchall()
    conn.close()
    return data

def read_receiver():
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM receivers')
    data = c.fetchall()
    conn.close()
    return data

def read_foodlisting():
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM food_listings')
    data = c.fetchall()
    conn.close()
    return data

def read_claim():
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM claims')
    data = c.fetchall()
    conn.close()
    return data

@st.cache_data
def add_provider(name,type,address,city,contact):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO providers (name, type,address,city,contact) VALUES (?,?,?,?,?)', (name,type,address,city,contact))
    conn.commit()
    conn.close()

@st.cache_data
def add_receiver(name,type,city,contact):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO receivers (name,type,city,contact) VALUES (?,?,?,?)', (name,type,city,contact))
    conn.commit()
    conn.close()

@st.cache_data
def add_foodlisting(food_name,quantity,expiry_date,provider_id,provider_type,location,food_type,meal_type):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO food_listings (food_name,quantity,expiry_date,provider_id,provider_type,location,food_type,meal_type) VALUES (?,?,?,?,?,?,?,?)', (food_name,quantity,expiry_date,provider_id,provider_type,location,food_type,meal_type))
    conn.commit()
    conn.close()

@st.cache_data
def add_claim(food_id,receiver_id,status,time_stamp):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO claims (food_id,receiver_id,status,time_stamp) VALUES (?,?,?,?)', (food_id,receiver_id,status,time_stamp))
    conn.commit()
    conn.close()

@st.cache_data
def update_provider(provider_id, name=None, type=None, address=None, city=None, contact=None):
    conn = sqlite3.connect('food_waste_management.db')
    cursor = conn.cursor()
    
    if name:
        cursor.execute('UPDATE providers SET name = ? WHERE provider_id = ?', (name, provider_id))
    if type:
        cursor.execute('UPDATE providers SET type = ? WHERE provider_id = ?', (type, provider_id))
    if address:
        cursor.execute('UPDATE providers SET address = ? WHERE provider_id = ?', (address, provider_id))
    if city:
        cursor.execute('UPDATE providers SET city = ? WHERE provider_id = ?', (city, provider_id))
    if address:
        cursor.execute('UPDATE providers SET contact = ? WHERE provider_id = ?', (contact, provider_id))
    
    conn.commit()
    conn.close()

@st.cache_data
def update_receiver(receiver_id, name=None, type=None, city=None, contact=None):
    conn = sqlite3.connect('food_waste_management.db')
    cursor = conn.cursor()
    
    if name:
        cursor.execute('UPDATE receivers SET name = ? WHERE receiver_id = ?', (name, receiver_id))
    if type:
        cursor.execute('UPDATE receivers SET type = ? WHERE receiver_id = ?', (type, receiver_id))
    if city:
        cursor.execute('UPDATE receivers SET city = ? WHERE receiver_id = ?', (city, receiver_id))
    if contact:
        cursor.execute('UPDATE receivers SET contact = ? WHERE receiver_id = ?', (contact, receiver_id))
    
    conn.commit()
    conn.close()

@st.cache_data
def update_foodlisting(food_id, food_name=None, quantity=None,expiry_date=None,provider_id=None,provider_type=None,location=None,food_type=None,meal_type=None):
    conn = sqlite3.connect('food_waste_management.db')
    cursor = conn.cursor()
    
    if food_name:
        cursor.execute('UPDATE food_listings SET food_name = ? WHERE food_id = ?', (food_name, food_id))
    if quantity:
        cursor.execute('UPDATE food_listings SET quantity = ? WHERE food_id = ?', (quantity, food_id))
    if expiry_date:
        cursor.execute('UPDATE food_listings SET expiry_date = ? WHERE food_id = ?', (expiry_date, food_id))
    if provider_id:
        cursor.execute('UPDATE food_listings SET provider_id = ? WHERE food_id = ?', (provider_id, food_id))
    if provider_type:
        cursor.execute('UPDATE food_listings SET provider_type = ? WHERE food_id = ?', (provider_type, food_id))
    if location:
        cursor.execute('UPDATE food_listings SET location = ? WHERE food_id = ?', (location, food_id))
    if food_type:
        cursor.execute('UPDATE food_listings SET food_type = ? WHERE food_id = ?', (food_type, food_id))
    if meal_type:
        cursor.execute('UPDATE food_listings SET meal_type = ? WHERE food_id = ?', (meal_type, food_id))
    
    conn.commit()
    conn.close()

@st.cache_data
def update_claim(claim_id,food_id=None,receiver_id=None,status=None,time_stamp=None):
    conn = sqlite3.connect('food_waste_management.db')
    cursor = conn.cursor()
    
    if food_id:
        cursor.execute('UPDATE claims SET food_id = ? WHERE claim_id = ?', (food_id, claim_id))
    if receiver_id:
        cursor.execute('UPDATE claims SET receiver_id = ? WHERE claim_id = ?', (receiver_id, claim_id))
    if status:
        cursor.execute('UPDATE claims SET status = ? WHERE claim_id = ?', (status, claim_id))
    if time_stamp:
        cursor.execute('UPDATE claims SET time_stamp = ? WHERE claim_id = ?', (time_stamp, claim_id))
    
    conn.commit()
    conn.close()

@st.cache_data
def delete_provider(provider_id):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM providers WHERE provider_id = ?', (provider_id,))
    conn.commit()
    conn.close()

@st.cache_data
def delete_receiver(receiver_id):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM receivers WHERE receiver_id = ?', (receiver_id,))
    conn.commit()
    conn.close()

@st.cache_data
def delete_foodlisting(food_id):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM food_listings WHERE food_id = ?', (food_id,))
    conn.commit()
    conn.close()

@st.cache_data
def delete_claim(claim_id):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM claims WHERE claim_id = ?', (claim_id,))
    conn.commit()
    conn.close()

@st.cache_data
def contact_provider(primary_key):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('select name,type,address,city,contact FROM providers WHERE provider_id = ?', (primary_key,))
    result = c.fetchone()
    return result
    conn.commit()
    conn.close()

@st.cache_data
def contact_receiver(primary_key):
    conn = sqlite3.connect('food_waste_management.db')
    c = conn.cursor()
    c.execute('select name,type,city,contact FROM receivers WHERE receiver_id = ?', (primary_key,))
    result = c.fetchone()
    return result
    conn.commit()
    conn.close()



if page=="Home":

    st.title("Local Food Waste Management")

    os.chmod("project_1titlepic.jpg",0o777)
    st.image("project_1titlepic.jpg",width=650)

    st.markdown("""Food waste is a major worldwide problem that affects society, the economy, and the environment. The waste of perfectly good food exposes inefficiencies in production, distribution, and consumption, wastes resources like water and energy, and adds to greenhouse gas emissions in landfills. Remarkably, tonnes of food go uneaten every year, and millions of people suffer from hunger.
                
    One effective strategy to cut waste and assist those in need is to manage extra food locally.           
                """)
    
elif page=="Information":

    st.title("🔍 Database Information")


    options = ['Select Any','Providers','Receivers','Food Listings','Claims']

    choice = st.selectbox('Select to view information',options)

    if choice == 'Providers':
        if st.button('View'):
            provider = read_provider()
            df = pd.DataFrame(provider, columns=['provider_id','name','type','address','city','contact'])
            st.dataframe(df)
        name_filter = st.sidebar.text_input('Filter by name:')
        type_filter = st.sidebar.multiselect('Filter by type:',['Supermarket','Grocery Store','Restaurant','Catering Service'])
        city_filter = st.sidebar.text_input('Filter by City:')
        query = "SELECT * FROM providers WHERE name LIKE ? AND city LIKE ?"
        params = (f'%{name_filter}%',f'%{city_filter}%')
        df = pd.read_sql_query(query, connection, params=params)      
        if type_filter:
            query += " AND type IN ({})".format(','.join('?' * len(type_filter)))
            params += tuple(type_filter)
            filter = pd.read_sql_query(query, connection, params=params)
            if name_filter or type_filter or city_filter:
                if st.sidebar.button("Filter"):
                    st.write(filter)

    elif choice == 'Receivers':
        if st.button('View'):
            receiver = read_receiver()
            df = pd.DataFrame(receiver, columns=['receiver_id','name','type','city','contact'])
            st.dataframe(df)
        name_filter = st.sidebar.text_input('Filter by name:')
        type_filter = st.sidebar.multiselect('Filter by type:',['Shelter','Individual','NGO','Charity'])
        city_filter = st.sidebar.text_input('Filter by City:')
        query = "SELECT * FROM receivers WHERE name LIKE ? AND city LIKE ? "
        params = (f'%{name_filter}%',f'%{city_filter}%')
        df = pd.read_sql_query(query, connection, params=params)      
        if type_filter:
            query += " AND type IN ({})".format(','.join('?' * len(type_filter)))
            params += tuple(type_filter)
            filter = pd.read_sql_query(query, connection, params=params)
            if name_filter or type_filter or city_filter:
                if st.sidebar.button("Filter"):
                    st.write(filter)

    elif choice == 'Food Listings':
        if st.button('View'):
            food_listings = read_foodlisting()
            df = pd.DataFrame(food_listings, columns=['food_id','food_name','quantity','expiry_date','provider_id','provider_type','location','food_type','meal_type'])
            st.dataframe(df)
        foodname_filter = st.sidebar.text_input('Filter by food_name:')
        providertype_filter = st.sidebar.multiselect('Filter by provider type:',['Grocery Store','Catering Service','Restaurant','Supermarket',])
        location_filter = st.sidebar.text_input('Filter by Location:')
        foodtype_filter = st.sidebar.multiselect('Filter by food type:',['Non-Vegetarian','Vegan','Vegetarian'])
        mealtype_filter = st.sidebar.multiselect('Filter by meal type:',['Breakfast','Dinner','Lunch','Snacks'])
        query = "SELECT * FROM food_listings WHERE food_name LIKE ? AND Location LIKE ? "
        params = (f'%{foodname_filter}%',f'%{location_filter}%')
        df = pd.read_sql_query(query, connection, params=params)      
        if providertype_filter:
            query += " AND provider_type IN ({})".format(','.join('?' * len(providertype_filter)))
            params += tuple(providertype_filter)
        if foodtype_filter:
            query += " AND food_type IN ({})".format(','.join('?' * len(foodtype_filter)))
            params += tuple(foodtype_filter)
        if mealtype_filter:
            query += " AND meal_type IN ({})".format(','.join('?' * len(mealtype_filter)))
            params += tuple(mealtype_filter)
        filter = pd.read_sql_query(query, connection, params=params)
        if foodname_filter or providertype_filter or location_filter or foodtype_filter or mealtype_filter:
            if st.sidebar.button("Filter"):
                st.write(filter)
    elif choice == 'Claims':
        if st.button('View'):
            claims = read_claim()
            df = pd.DataFrame(claims, columns=['claim_id','food_id','receiver_id','status','time_stamp'])
            st.dataframe(df)
        status_filter = st.sidebar.multiselect('Filter by status:',['Completed','Pending','Cancelled'])
        query = "SELECT * FROM claims"
        params = ()
        df = pd.read_sql_query(query, connection, params=params)      
        if status_filter:
            query += " WHERE status IN ({})".format(','.join('?' * len(status_filter)))
            params += tuple(status_filter)
            filter = pd.read_sql_query(query, connection, params=params)
            if status_filter:
                if st.sidebar.button("Filter"):
                    st.write(filter)
    else:
        st.write("Please select an option to display content.")

elif page=="Crud Operations":

    st.title("⚙️ Information Feed")

    action = st.selectbox("Choose an action",['Select any Action','Add','Update','Delete'])

    if action == 'Add':
        option = st.selectbox('Choose a Table:', ['Provider', 'Receiver','Food_listings','Claims'])
        if option == 'Provider':
            name = st.text_input("Enter your name")
            type = st.selectbox('Choose a Type:',['Supermarket','Grocery Store','Restaurant','Catering Service'])
            address = st.text_area("Provide your address")
            city = st.text_input("Enter city name")
            contact = st.text_input("Enter your contact")
            if name and address and city and contact:
                if st.button("Submit"):
                    add_provider(name,type,address,city,contact)
                    st.success(f"Hello {name}, Registration Successful")
            else:
                st.warning("Please fill in all fields to enable the button.")
        
        elif option == 'Receiver':
            name = st.text_input("Enter your name")
            type = st.selectbox('Choose a Type:',['Shelter','Individual','NGO','Charity'])
            city = st.text_input("Enter city name")
            contact = st.text_input("Enter your contact")
            if name and city and contact:
                if st.button("Submit"):
                    add_receiver(name,type,city,contact)
                    st.success(f"Hello {name}, Registration Successful")
            else:
                st.warning("Please fill in all fields to enable the button.")

        elif option == 'Food_listings':
            food_name = st.text_input("Enter food name")
            quantity = st.slider("Select quantity",1,100)
            expiry_date = st.date_input("Select expiry date")
            provider_id = st.text_input("Enter provider id")
            provider_type = st.selectbox('Choose a Type:',['Supermarket','Grocery Store','Restaurant','Catering Service'])
            location = st.text_input("Enter location")
            food_type = st.selectbox('Choose a food type:',['Non-Vegetarian','Vegan','Vegetarian'])
            meal_type = st.selectbox('Choose a meal type:',['Breakfast','Dinner','Lunch','Snacks'])
            if provider_id and location and food_name:
                    if st.button("Add Food"):
                        add_foodlisting(food_name,quantity,expiry_date,provider_id,provider_type,location,food_type,meal_type)
                        st.success("Food listed sucessfully")
            else:
                st.warning("Please fill in all fields to enable the button.")

        elif option == 'Claims':
            food_id = st.text_input("Enter food id")
            receiver_id = st.text_input("Enter receiver id")
            status = st.selectbox('Choose a status:',['Completed','Pending','Cancelled'])
            date = st.date_input('Choose a date:',datetime.now().date())
            time = st.time_input("Select a time", datetime.now().time())
            time_stamp = datetime.combine(date,time)
            if food_id and receiver_id :
                    if st.button("claim"):
                        add_claim(food_id,receiver_id,status,time_stamp)
                        st.success("Claim information added sucessfully")
            else:
                st.warning("Please fill in all fields to enable the button.")
        
    if action == 'Update':
        option = st.selectbox('Choose a Table:', ['Provider', 'Receiver','Food_listings','Claims'])
        if option == 'Provider':
            provider_id = st.number_input("Enter Provider_id",min_value=1,max_value=2000,step=1)
            name = st.text_input("Enter name")
            type = st.selectbox('Choose a Type:',['Supermarket','Grocery Store','Restaurant','Catering Service'])
            address = st.text_area("Provide your address")
            city = st.text_input("Enter city")
            contact = st.text_input("Enter Contact information")
            if st.button("Update"):
                update_provider(provider_id, name if name else None, type if type else None, address if address else None, city if city else None, contact if contact else None)
                st.success("Provider information updated sucessfully")
            else:
                st.warning("Please fill in fields that need to be updated")

        if option == 'Receiver':
            receiver_id = st.number_input("Enter receiver_id",min_value=1,max_value=2000,step=1)
            name = st.text_input("Enter name")
            type = st.selectbox('Choose a Type:',['Shelter','Individual','NGO','Charity'])
            city = st.text_input("Enter city")
            contact = st.text_input("Enter Contact information")
            if st.button("Update"):
                update_receiver(receiver_id, name if name else None, type if type else None, city if city else None, contact if contact else None)
                st.success("Receiver information updated sucessfully")
            else:
                st.warning("Please fill in fields that need to be updated")

        if option == 'Food_listings':
            food_id = st.number_input("Enter food_id",min_value=1,max_value=2000,step=1)
            food_name = st.text_input("Enter food name")
            quantity = st.slider("Select quantity",1,100)
            expiry_date = st.date_input("Select expiry date")
            provider_id = st.text_input("Enter provider id")
            provider_type = st.selectbox('Choose a Type:',['Supermarket','Grocery Store','Restaurant','Catering Service'])
            location = st.text_input("Enter location")
            food_type = st.selectbox('Choose a food type:',['Non-Vegetarian','Vegan','Vegetarian'])
            meal_type = st.selectbox('Choose a meal type:',['Breakfast','Dinner','Lunch','Snacks'])
            if st.button("Update"):
                update_foodlisting(food_id, food_name if food_name else None, quantity if quantity else None, expiry_date if expiry_date else None, provider_id if provider_id else None, provider_type if provider_type else None,location if location else None, food_type if food_type else None, meal_type if meal_type else None)
                st.success("Food listing information updated sucessfully")
            else:
                st.warning("Please fill in fields that need to be updated")

        if option == 'Claims':
            claim_id = st.number_input("Enter claim_id",min_value=1,max_value=2000,step=1)
            food_id = st.text_input("Enter food id")
            receiver_id = st.text_input("Enter receiver id")
            status = st.selectbox('Choose a status:',['Completed','Pending','Cancelled'])
            date = st.date_input('Choose a date:',datetime.now().date())
            time = st.time_input("Select a time", datetime.now().time())
            time_stamp = datetime.combine(date,time)
            if st.button("Update"):
                update_claim(claim_id, food_id if food_id else None, receiver_id if receiver_id else None, status if status else None, time_stamp if time_stamp else None)
                st.success("Clain information updated sucessfully")
            else:
                st.warning("Please fill in fields that need to be updated")

    if action == 'Delete':
        option = st.selectbox('Choose a Table:', ['Provider', 'Receiver','Food_listings','Claims'])
        if option == 'Provider':
            provider_id = st.number_input("Enter Provider_id",min_value=1,max_value=2000,step=1)
            if st.button("Delete"):
                delete_provider(provider_id)
                st.success("Provider information deleted sucessfully")
            else:
                st.warning("Please fill in provider_id to delete the information")
        
        if option == 'Receiver':
            receiver_id = st.number_input("Enter receiver_id",min_value=1,max_value=2000,step=1)
            if st.button("Delete"):
                delete_receiver(receiver_id)
                st.success("Receiver information deleted sucessfully")
            else:
                st.warning("Please fill in receiver_id to delete the information")

        if option == 'Food_listings':
            food_id = st.number_input("Enter food_id",min_value=1,max_value=2000,step=1)
            if st.button("Delete"):
                delete_foodlisting(food_id)
                st.success("Food Listing information deleted sucessfully")
            else:
                st.warning("Please fill in Food_id to delete the information")

        if option == 'Claims':
            claim_id = st.number_input("Enter claim_id",min_value=1,max_value=2000,step=1)
            if st.button("Delete"):
                delete_claim(claim_id)
                st.success("Claim information deleted sucessfully")
            else:
                st.warning("Please fill in claim_id to delete the information")

    else:
        st.write("Please Choose an Action")

elif page=="Queries":

    st.title("📊 Analysis")

    providers = pd.read_csv("providers_data.csv")
    receivers = pd.read_csv("receivers_data.csv")
    food_listings = pd.read_csv("food_listings_data.csv")
    claims = pd.read_csv("claims_data.csv")

    connection = sqlite3.connect("food_waste_management.db")
    cursor = connection.cursor()

    #query 1.How many food providers and receivers are there in each city?
    query_1_1 = ('''
                select city, count(provider_id) from providers group by city;
    ''')
    query_1_2 = ('''
                select city, count(receiver_id) from receivers group by city;
    ''')

    cursor.execute(query_1_1)
    result_1_1 = cursor.fetchall()

    cursor.execute(query_1_2)
    result_1_2 = cursor.fetchall()

    df_1_1 = pd.DataFrame(result_1_1,columns=["City","no_of_food_providers"])
    df_1_2 = pd.DataFrame(result_1_2,columns=["city","no_of_food_receivers"])

    combined_df = pd.concat([df_1_1, df_1_2], axis=1, ignore_index=False)

    #query 2.Which type of food provider (restaurant, grocery store, etc.) contributes the most food?
    query_2 = ('''
                select provider_type,sum(quantity) as contributed_food
                from food_listings
                group by provider_type
                order by sum(quantity) desc
                limit 1;
    ''')

    cursor.execute(query_2)
    result_2 = cursor.fetchall()

    df_2 = pd.DataFrame(result_2,columns=["provider_type","contributed_food"])

    #query 3.What is the contact information of food providers in a specific city?
    query_3 = ('''
                SELECT name,contact FROM providers
                group by city;
    ''')

    cursor.execute(query_3)
    result_3 = cursor.fetchall()

    df_3 = pd.DataFrame(result_3,columns=["provider_name","contact"])

    #query 4.Which receivers have claimed the most food?
    query_4 = ('''
                select receivers.name, sum(food_listings.quantity) as food_claimed
                from receivers
                inner join claims on receivers.receiver_id = claims.receiver_id
                inner join food_listings on food_listings.food_id = claims.food_id
                group by receivers.receiver_id
                order by food_claimed desc
                limit 10;
    ''')

    cursor.execute(query_4)
    result_4 = cursor.fetchall()

    df_4 = pd.DataFrame(result_4,columns=["receiver_name","food_claimed"])

    #query 5.What is the total quantity of food available from all providers?
    query_5 = ('''
                select sum(quantity) as total_quantity_of_food_available
                from food_listings
                inner join claims on claims.Food_id = food_listings.Food_id
                where claims.status != 'completed';
    ''')

    cursor.execute(query_5)
    result_5 = cursor.fetchall()

    df_5 = pd.DataFrame(result_5,columns=["total_quantity_of_food_available"])

    #query 6.Which city has the highest number of food listings?
    query_6 = ('''
                select location,sum(quantity) as food_listed 
                from food_listings
                group by location
                order by food_listed desc
                limit 1;
    ''')

    cursor.execute(query_6)
    result_6 = cursor.fetchall()

    df_6 = pd.DataFrame(result_6,columns=["location","food_listed"])

    #query 7.What are the most commonly available food types?
    query_7 = ('''
                select distinct(Food_type) as food_types
                from food_listings
    ''')

    cursor.execute(query_7)
    result_7 = cursor.fetchall()

    df_7 = pd.DataFrame(result_7,columns=["food_types"])


    #query  9.How many food claims have been made for each food item?
    query_9 = ('''
                select food_name,count(claims.food_id) as no_of_claims
                from food_listings
                inner join claims on claims.food_id = food_listings.food_id
                group by food_name;
    ''')

    cursor.execute(query_9)
    result_9 = cursor.fetchall()

    df_9 = pd.DataFrame(result_9,columns=["food_name","no_of_claims"])

    #query  10.Which provider has had the highest number of successful food claims?
    query_10 = ('''
                select providers.name, count(claims.status) as sucessful_food_claims
                from providers
                inner join food_listings on providers.provider_id = food_listings.provider_id
                inner join claims on claims.food_id = food_listings.food_id
                where claims.status = 'Completed'
                group by providers.provider_id
                order by sucessful_food_claims desc
                limit 1;
    ''')

    cursor.execute(query_10)
    result_10 = cursor.fetchall()

    df_10 = pd.DataFrame(result_10,columns=["provider_name","Sucessful_food_claims"])

    #query  12.What percentage of food claims are completed vs. pending vs. canceled?
    query_12 = ('''
                select (select (count(status)*100)/(select count(*) from claims)
                from claims 
                where status = "Completed"),(select (count(status)*100)/(select count(*) from claims)
                from claims 
                where status = "Pending"),(select (count(status)*100)/(select count(*) from claims)
                from claims 
                where status = "Cancelled") from claims
                limit 1;
    ''')

    cursor.execute(query_12)
    result_12 = cursor.fetchall()

    df_12 = pd.DataFrame(result_12,columns=["completed","pending","cancelled"])

    #query  13.What is the average quantity of food claimed per receiver?
    query_13 = ('''
                    select receivers.name,avg(food_listings.quantity) as average_quantity_of_food_claimed_per_receiver
                    from food_listings
                    inner join claims on food_listings.food_id = claims.food_id
                    inner join receivers on claims.receiver_id = receivers.receiver_id
                    group by receivers.receiver_id;
    ''')

    cursor.execute(query_13)
    result_13 = cursor.fetchall()

    df_13 = pd.DataFrame(result_13,columns=["receiver_name","average_quantity_of_food_claimed_per_receiver"])

    #query  14.Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?
    query_14 = ('''
                    select food_listings.meal_type as meal_type,count(claims.claim_id)
                    from food_listings
                    inner join claims on claims.food_id = food_listings.food_id 
                    where claims.status = 'Completed'
                    group by food_listings.meal_type
                    order by count(claims.claim_id)
                    limit 1;
    ''')

    cursor.execute(query_14)
    result_14 = cursor.fetchall()

    df_14 = pd.DataFrame(result_14,columns=["meal_type","no_of_claims"])

    #query  15.What is the total quantity of food donated by each provider?
    query_15 = ('''
                    select providers.name,sum(food_listings.quantity)
                    from providers
                    inner join food_listings on food_listings.provider_id = providers.provider_id
                    group by providers.name; 
    ''')

    cursor.execute(query_15)
    result_15 = cursor.fetchall()

    df_15 = pd.DataFrame(result_15,columns=["provider_name","quantity_donated"])

    dataframes_1 = {
        'Number of Providers and Receivers in each city': combined_df,
        'Type of Provider contributing Most food': df_2,
        'Contact information of Food Providers in each city':df_3,
        'Top 10 receivers who claimed most food':df_4,
        'Quantity of food available':df_5,
        'City with highest number of food listings':df_6,
        'Most commonly available food types':df_7,
        'Number of food claims made for each food item':df_9,
        'Provider with highest number of sucessful food claims':df_10,
        'Percentage of food claim status':df_12,
        'Average quantity of food claimed per receiver':df_13,
        'Most claimed meal type':df_14,
        'Total quantity of food donated by each provider':df_15
        
    }

    selected_dfs_1 = st.selectbox("Select Table",list(dataframes_1.keys()))

    st.dataframe(dataframes_1[selected_dfs_1])

elif page=="Learner Queries":

    st.title("📈 Learner Analysis")

    providers = pd.read_csv("providers_data.csv")
    receivers = pd.read_csv("receivers_data.csv")
    food_listings = pd.read_csv("food_listings_data.csv")
    claims = pd.read_csv("claims_data.csv")

    connection = sqlite3.connect("food_waste_management.db")
    cursor = connection.cursor()

    #query  16.which provider type have provided the least food?
    query_16 = ('''
                    select providers.type, sum(food_listings.quantity)
                    from providers
                    inner join food_listings on food_listings.provider_id = providers.provider_id
                    group by providers.type
                    order by sum(food_listings.quantity) asc
                    limit 1 ;   
    ''')

    cursor.execute(query_16)
    result_16 = cursor.fetchall()

    df_16 = pd.DataFrame(result_16,columns=["provider_type","quantity"])

    #query  17.which city have more providers ?
    query_17 = ('''
                    select city,count(provider_id)
                    from providers
                    group by city
                    order by count(provider_id) desc
                    limit 1;               
    ''')

    cursor.execute(query_17)
    result_17 = cursor.fetchall()

    df_17 = pd.DataFrame(result_17,columns=["city","no_of_providers"])

    #query  18.which type of receivers claimed more food
    query_18 = ('''
                    select receivers.type ,sum(quantity)
                    from receivers
                    inner join claims on claims.receiver_id = receivers.receiver_id
                    inner join food_listings on food_listings.food_id = claims.food_id
                    group by receivers.type
                    order by sum(quantity) desc
                    limit 1;     
    ''')

    cursor.execute(query_18)
    result_18 = cursor.fetchall()

    df_18 = pd.DataFrame(result_18,columns=["receiver_type","food_claimed"])

    #query  19.top 5 city has low number of food listings
    query_19 = ('''
                    select location, sum(quantity) as quantity_listed
                    from food_listings
                    group by location
                    order by quantity_listed asc
                    limit 5;                  
    ''')

    cursor.execute(query_19)
    result_19 = cursor.fetchall()

    df_19 = pd.DataFrame(result_19,columns=["city_name","food_listed"])

    #query  20.top 10 provider has provided vegan foodtype
    query_20 = ('''
                    select providers.name as provider_name
                    from providers
                    join food_listings on food_listings.provider_id = providers.provider_id
                    where food_listings.food_type = 'Vegan'
                    order by food_listings.quantity desc
                    limit 10;               
    ''')

    cursor.execute(query_20)
    result_20 = cursor.fetchall()

    df_20 = pd.DataFrame(result_20,columns=["provider_name"])

    #query  21.what is the average quantity of food donated by each provider
    query_21 = ('''
                    select providers.name as provider_name,avg(food_listings.quantity) as average_quantity_of_food
                    from providers
                    inner join food_listings on providers.provider_id = food_listings.provider_id
                    group by providers.provider_id               
    ''')

    cursor.execute(query_21)
    result_21 = cursor.fetchall()

    df_21 = pd.DataFrame(result_21,columns=["provider_name","average_quantity_of_food"])

    #query  22.list top 5 provider
    query_22 = ('''
                    select providers.Name as provider_name, sum(food_listings.quantity) as food_contributed
                    from providers
                    inner join food_listings on providers.provider_id = food_listings.provider_id
                    group by food_listings.provider_id
                    order by food_contributed desc
                    limit 5;
                    
    ''')

    cursor.execute(query_22)
    result_22 = cursor.fetchall()

    df_22 = pd.DataFrame(result_22,columns=["provider_name","Food_contributed"])


    dataframes_2 = {
        'Type of provider provided least quantity of food':df_16,
        'City with more providers':df_17,
        'Type of receivers claiming more food':df_18,
        'Top 5 City with low number of food listings':df_19,
        'Top 10 provider who provides vegan food type':df_20,
        'Average quantity of food donated by each provider':df_21,
        'Top 5 provider of food with food contributed':df_22
        
    }

    selected_dfs_2 = st.selectbox("Select Table",list(dataframes_2.keys()))

    st.write(dataframes_2[selected_dfs_2])

elif page=="Contact":

    st.title("📞 Contact Information")


    option = st.selectbox("Select an option:",['Select any','Provider','Receiver'])
    if option == 'Provider':
        primary_key = st.text_input("Enter Provider_id")
        if primary_key:
            if st.button("View"):
                filter = pd.DataFrame(contact_provider(primary_key),columns=["Provider_Information"])
                filter.index = [''] * len(filter)
                st.table(filter)
        else:
            st.warning("Please fill in provider_id to view contact information")

    if option == 'Receiver':
        primary_key = st.text_input("Enter receiver_id")
        if primary_key:
            if st.button("View"):
                filter = pd.DataFrame(contact_receiver(primary_key),columns=["Receiver_Information"])
                filter.index = [''] * len(filter)
                st.table(filter)
        else:
            st.warning("Please fill in provider_id to view contact information")

elif page=="Feedback":

    st.title("📝 Feedback Form")

    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    Type = st.selectbox('choose a Type:',['Provider','Receiver','other'])
    contact = st.text_input("enter your contact number")
    feedback = st.text_area("Give your feedback")
    if first_name and last_name and contact and feedback:
                if st.button("Submit"):
                    st.success("Thanks for submitting your feedback")
    else:
        st.warning("Please fill in all fields to enable the button.")

elif page=="Creator":

    st.title("👩‍💻 Creator Information")

    st.subheader("Shreeja S")
    os.chmod("project_1creatorpic.jpg",0o777)
    st.image("project_1creatorpic.jpg", width=200)
    st.subheader("Pursuing")
    st.markdown("Advanced Programmer with Data Science Mastery Program by **GUVI**")
