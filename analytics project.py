# importing libraries
from datetime import datetime
import datetime
import logging
import sqlite3
from faker import Faker
from flask import Flask, request, jsonify, redirect, url_for
import random

# creating faker variable
fake = Faker()
# creating Flask variable giving standard name app
app = Flask(__name__)
# config for cookies protection
app.config['SECRET_KEY'] = 'DABM'


class SystemUsers:
    def __init__(self, UserID, Username, Password, UserRole):
        self.UserID = UserID
        self.Username = Username
        self.Password = Password
        self.UserRole = UserRole


class Transactions:
    def __init__(self, TransactionID, TransactionDateTime, Transactiontype, Amount, Party1ID, Party2ID,
                 TransactionStatus, Category, Comments):
        self.TransactionID = TransactionID
        self.TransactionDateTime = TransactionDateTime
        self.Transactiontype = Transactiontype
        self.Amount = Amount
        self.Party1ID = Party1ID
        self.Party2ID = Party2ID
        self.TransactionStatus = TransactionStatus
        self.Category = Category
        self.Comments = Comments


class TransactionsRules:
    def __init__(self, RuleID, RuleName, RuleDescription, ValidationQuery, UserID):
        self.RuleID = RuleID
        self.RuleName = RuleName
        self.RuleDescription = RuleDescription
        self.ValidationQuery = ValidationQuery
        self.UserID = UserID


class AuditTrail:
    def __init__(self, AuditID, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp):
        self.AuditID = AuditID
        self.UserID = UserID
        self.TransactionID = TransactionID
        self.ActionBy = ActionBy
        self.RuleName = RuleName
        self.ActionPerformed = ActionPerformed
        self.ActionTimestamp = ActionTimestamp


class Reports:
    def __init__(self, ReportID, ReportName, ReportType, GeneratedByUserID, GeneratedDateTime):
        self.ReportID = ReportID
        self.ReportName = ReportName
        self.ReportType = ReportType
        self.GeneratedByUserID = GeneratedByUserID
        self.GeneratedDateTime = GeneratedDateTime


try:
    with sqlite3.connect('tms.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
                     create table if not exists Users (
                       UserID INTEGER PRIMARY KEY,
                       Username TEXT(50) NOT NULL,
                       Password TEXT(100) NOT NULL,
                       UserRole TEXT(50) NOT NULL
                       )
        ''')

        cursor.execute('''
                      create table if not exists Transactions (
                        TransactionID integer primary key,
                        TransactionDateTime TimeStamp default CURRENT_TIMESTAMP,
                        Transactiontype text(50) not null,
                        Amount integer(10,2) not null,
                        Party1ID integer,
                        Party2ID integer,
                        TransactionStatus text(20) default 'Pending',
                        Category text(50),
                        Comments text(255),
                        Foreign Key (Party1ID) references Users(UserID),
                        Foreign Key (Party2ID) references Users(UserID)
                      )
        ''')
        cursor.execute('''                       
                      create table if not exists TransactionsRules(
                        RuleID integer primary key,
                        RuleName text(100) not null,
                        RuleDescription text(255),
                        ValidationQuery text(1000) not null,
                        UserID integer,
                        Foreign key (UserID) References Users(UserID)
                      )
        ''')
        cursor.execute('''
                       create table if not exists AuditTrail (
                        AuditID integer primary key,
                        UserID integer,
                        TransactionID integer,
                        ActionBy TimeStamp Default Current_TimeStamp,
                        RuleName text(500),
                        ActionPerformed text(1000) not null,
                        ActionTimestamp datetime default CURRENT_TIMESTAMP,
                        Foreign Key (UserID) References Users(UserID)
                        Foreign Key (TransactionID) References Transactions (TransactionID)
        )
        ''')
        cursor.execute('''
                      create table if not exists Reports (
                        ReportID integer primary key,
                        ReportName text(100) not null,
                        ReportType text(50) not null,
                        GeneratedByUserID integer,
                        GeneratedDateTime Timestamp default CURRENT_TIMESTAMP,
                        Foreign Key (GeneratedByUserID) References Users(UsersID)
                       )
        ''')

except Exception as e:
    print(f'Error during database creation: {e}')

with sqlite3.connect('tms.db') as connection:
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Users')

with sqlite3.connect('tms.db') as connection:
    cursor = connection.cursor()
    cursor.execute('DELETE FROM TRANSACTIONS')

with sqlite3.connect('tms.db') as connection:
    cursor = connection.cursor()
    cursor.execute('Delete From TransactionsRules')

with sqlite3.connect('tms.db') as connection:
    cursor = connection.cursor()
    cursor.execute('Delete From AuditTrail')

with sqlite3.connect('tms.db') as connection:
    cursor = connection.cursor()
    cursor.execute('Delete from Reports')

for i, user_role in enumerate(['Admin', 'Manager'], start=1):
    with sqlite3.connect('tms.db') as connection:
        cursor = connection.cursor()
        Username = user_role.lower()
        Password = f'{user_role.lower()}123'
        UserRole = user_role
        user = SystemUsers(i, Username, Password, UserRole)

        cursor.execute('''insert into Users (UserID, Username, Password, UserRole) values (?,?,?,?)
                             ''', (user.UserID, user.Username, user.Password, UserRole))

for i in range(3, 101):
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            Username = fake.user_name()
            Password = fake.password()
            UserRole = 'User'
            user = SystemUsers(i, Username, Password, UserRole)

            cursor.execute('''insert into Users (UserID, Username, Password, UserRole) values (?,?,?,?)
            ''', (user.UserID, user.Username, user.Password, user.UserRole))
    except sqlite3.Error as e:
        print(f'Error In The Loop Iteration {i} : {e}')

for i in range(3151, 3999):
    try:
        with (sqlite3.connect('tms.db') as connection):
            cursor = connection.cursor()
            TransactionDateTime = fake.date_time_between(start_date='-1y', end_date='now')
            Transactiontype = random.choice(('Credit', 'Debit'))
            Amount = random.randrange(1000, 20000)

            Party1ID = random.randint(2, 101)
            Party2ID = random.randint(2, 101)

            TransactionStatus = random.choice(('Approved', 'Declined', 'Pending', 'Failed'))
            Category = random.choice(['School fees', 'Groceries', 'Rent or mortgage payments',
                                      'Utilities (electricity, water, internet, etc.)',
                                      'Transportation (fuel, public transit fare, etc.)',
                                      'Healthcare (doctor’s visits, medication, etc.)',
                                      'Insurance (health, car, home, etc.)', 'Dining out',
                                      'Personal care (gym membership, beauty products, etc.)',
                                      'Shopping (clothing, electronics, etc.)', 'Childcare expenses',
                                      'Savings and investments',
                                      'Public transportation fares', 'Coffee and snacks', 'Lunch and dinner',
                                      'Grocery shopping',
                                      'Online subscriptions (music, video streaming, etc.)', 'Mobile phone bills',
                                      'Internet and cable bills',
                                      'Pet care expenses', 'Laundry and dry cleaning', 'Home maintenance costs',
                                      'Fitness and wellness expenses (gym, yoga classes, etc.)',
                                      'Books and magazines', 'Hobbies and leisure activities', 'Charitable donations',
                                      'Savings for vacation or big-ticket items'])

            Approved = random.choice((
                'Transaction successfully', 'Funds transferred successfully', 'Transfer initiated',
                'Payment processed', 'Transaction completed',
                'Funds moved to the designated account', 'Money sent successfully',
                'Payment completed', 'Transfer confirmed', 'Transaction finalized',
                'Funds dispatched successfully', 'Transfer executed', 'Transaction accomplished',
                'Money dispatched', 'Payment confirmed', 'Funds transferred successfully',
                'Payment dispatched', 'Transaction executed successfully', 'Funds moved',
                'Transfer confirmed successfully', 'Transaction successful', 'payment processed',
                'Funds dispatched successfully', 'Transfer completed', 'Money sent successfully',
                'Transaction finalized successfully', 'Transaction dispatched',
                'Transfer successful', 'Payment dispatched successfully', 'Transaction completed',
                'Funds transferred successfully'))

            Decline = random.choice(('Payment declined', 'insufficient funds', 'Transfer declined',
                                     'check account information', 'Declined transaction not authorized',
                                     'Payment declined', 'invalid card details', 'Transfer declined',
                                     'account verification failed', 'insufficient balance.', 'Transaction declined',
                                     'security check failed.', 'Transfer declined', 'suspicious activity.',
                                     'incorrect payment details', 'Payment declined suspicious activity',
                                     'transaction limit exceeded.', 'incorrect details', 'invalid account',
                                     'Declined, security verification failed',
                                     'technical issues', 'unauthorized transaction', 'Transaction declined',
                                     'please contact support'))

            Pending = random.choice(('Transaction is pending verification.', 'Payment pending approval.',
                                     'Transfer pending - awaiting confirmation.',
                                     'Pending - additional verification required.',
                                     'Payment processing, currently pending.', 'Transfer pending - under review.',
                                     'Pending approval - awaiting confirmation.', 'Transaction pending, please wait.',
                                     'Payment pending, verifying details.', 'Transfer pending approval.',
                                     'Transaction is pending verification.', 'Payment pending approval.',
                                     'Transfer pending - awaiting confirmation.',
                                     'Pending - additional verification required.',
                                     'Payment processing, currently pending.', 'Transfer pending - under review.',
                                     'Pending approval - awaiting confirmation.', 'Transaction pending, please wait.',
                                     'Payment pending, verifying details.', 'Transfer pending approval.'))

            Failed = random.choice(('Payment failed, please try again.', 'Transfer failed, account not found.',
                                    'Failed - incorrect recipient details.', 'Transaction failed, technical issues.',
                                    'Payment failed - card expired.', 'Transfer failed, network error.',
                                    'Failed - invalid transaction.', 'Transaction failed, account closed.',
                                    'Payment failed, transaction declined.', 'Transaction failed, please retry.',
                                    'Payment failed, check card details.',
                                    'Transfer failed - recipient account closed.',
                                    'Failed - network issues, try again.', 'Transaction failed - insufficient balance.',
                                    'Payment failed, security check not passed.',
                                    'Transfer failed - recipient not available.',
                                    'Failed - incorrect payment information.',
                                    'Transaction failed - technical difficulties.',
                                    'Payment failed, contact customer support.'))

            Comments = Approved if TransactionStatus == 'Approved' else \
                Decline if TransactionStatus == 'Declined' else \
                    Pending if TransactionStatus == 'Pending' else \
                        Failed if TransactionStatus == 'Failed' else None

            transactions = Transactions(i, TransactionDateTime, Transactiontype, Amount, Party1ID, Party2ID,
                                        TransactionStatus,
                                        Category, Comments)

            cursor.execute('''
                        insert into Transactions (TransactionID ,TransactionDateTime,
                        Transactiontype ,Amount, Party1ID ,Party2ID ,
                        TransactionStatus ,Category ,Comments) values (?,?,?,?,?,?,?,?,?)
                        ''',
                           (transactions.TransactionID, transactions.TransactionDateTime, transactions.Transactiontype,
                            transactions.Amount, transactions.Party1ID, transactions.Party2ID,
                            transactions.TransactionStatus,
                            transactions.Category, transactions.Comments))
    except sqlite3.Error as e:
        print(f'Error in loop iteration {i}: {e}')

for i in range(1, 201):
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            RuleName = random.choice(('Sum_Credit', 'Sum_Debit', 'Count_Credit', 'Count_Debit'))
            ruledescription = {
                'Sum_Credit': ['Will Provide Sum Of Credited Transaction on The Basis of Transaction User'],
                'Sum_Debit': ['Will Provide Sum Of Debited Transaction on The Basis of Transaction User'],
                'Count_Credit': ['Will Provide Count Of Credited Transaction on The Basis of Transaction User'],
                'Count_Debit': ['Will Provide Count Of Debited Transaction of Basis on The Transaction User']
            }
            RuleDescription = random.choice(ruledescription[RuleName])
            UserID = random.randint(2, 101)

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                    FROM Transactions
                    INNER JOIN Users ON Users.UserID = Transactions.Party1ID OR 
                    Users.UserID = Transactions.Party2ID
                    WHERE 
                '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f" AND Users.UserID = {UserID}"

                result = cursor.execute(query_rule).fetchone()

                ValidationQuery = 'Please Enter Valid Value' if result is None else result[0]

                ValidationQuery = 'No Transaction' if ValidationQuery is None else ValidationQuery
                transactionsrules = TransactionsRules(i, RuleName, RuleDescription, ValidationQuery, UserID)

                cursor.execute('''
                               INSERT INTO TransactionsRules
                               (RuleID, RuleName, RuleDescription, ValidationQuery, UserID)
                               VALUES (?,?,?,?,?)
                               ''',
                               (transactionsrules.RuleID, transactionsrules.RuleName, transactionsrules.RuleDescription,
                                transactionsrules.ValidationQuery, transactionsrules.UserID))
    except sqlite3.Error as e:
        print(f'Error in loop iteration {i}: {e}')

for i in range(1, 201):
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()

            UserID = random.randint(2, 101)
            TransactionID = random.randint(3151, 3999)
            RuleName = random.choice(('Sum_Credit', 'Sum_Debit', 'Count_Credit', 'Count_Debit'))
            one_year_ago = fake.date_time_between(start_date='-1y', end_date='now')
            Start_Date = one_year_ago
            End_Date = (one_year_ago + datetime.timedelta(days=random.randint(1, 365)))

            ActionBy = f'{Start_Date} to {End_Date}'

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                    FROM Transactions
                    INNER JOIN AuditTrail ON AuditTrail.UserID = Transactions.Party1ID OR 
                    AuditTrail.UserID = Transactions.Party2ID
                    WHERE 
                '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f" AND AuditTrail.UserID = {UserID} AND date(Transactions.TransactionDateTime) BETWEEN DATE('{Start_Date}') AND DATE('{End_Date}')"

                result = cursor.execute(query_rule).fetchone()

                ActionPerformed = 'Please Enter Valid Value' if result is None else result[0]

                ActionPerformed = 'No Transaction' if ActionPerformed is None else ActionPerformed
            if ActionBy:
                cursor.execute('''
                select * from Transactions
                inner join AuditTrail on AuditTrail.UserID = Transactions.Party1ID
                or AuditTrail.UserID = Transactions.Party2ID
                where date(Transactions.TransactionDateTime) BETWEEN DATE(?) AND DATE(?) 
                and UserID = ?
                ''', (Start_Date, End_Date, UserID,)).fetchall()

            ActionTimestamp = datetime.datetime.now()
            audittrail = AuditTrail(i, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp)
            cursor.execute('''
                INSERT INTO AuditTrail
                (AuditID, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                audittrail.AuditID, audittrail.UserID, audittrail.TransactionID, audittrail.ActionBy,
                audittrail.RuleName, audittrail.ActionPerformed, audittrail.ActionTimestamp))
    except sqlite3.Error as e:
        print(f'The Iteration Error {i} : {e}')

for i in range(1, 101):
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            one_year_ago = fake.date_time_between(start_date='-1y', end_date='now')
            Start_Date = one_year_ago
            End_Date = (one_year_ago + datetime.timedelta(days=random.randint(1, 365)))
            GeneratedByUserID = random.randint(2, 101)
            ReportName = cursor.execute('''
                select * from Transactions
                inner join Reports on Reports.GeneratedByUserID = Transactions.Party1ID
                or Reports.GeneratedByUserID = Transactions.Party2ID
                where date(Transactions.TransactionDateTime) BETWEEN DATE(?) AND DATE(?) 
                and UserID = ?
                ''', (Start_Date, End_Date, GeneratedByUserID,)).fetchall()

            ReportType = random.choice(
                ('sum', 'count', 'Count_salesCredit', 'Count_salesDebit', 'Sum_salesCredit', 'Sum_salesDebit',
                 'UserCount', 'TransactionCount', 'Sum_Category', 'Count_Category', 'Sum_Amount'))
            if ReportType in (
                    'sum', 'count', 'Count_salesCredit', 'Count_salesDebit', 'Sum_salesCredit', 'Sum_salesDebit'):
                query = f'''
                                SELECT {ReportType}(Amount) AS Result
                                FROM Transactions
                                WHERE date(TransactionDateTime) BETWEEN DATE(?) AND DATE(?)
                                AND (Party1ID = ? OR Party2ID = ?)
                            '''
                result = \
                    cursor.execute(query, (Start_Date, End_Date, GeneratedByUserID, GeneratedByUserID)).fetchone()[0]
            elif ReportType == 'UserCount':
                query = '''
                                SELECT COUNT(DISTINCT UserID) AS Result
                                FROM Transactions
                                WHERE date(TransactionDateTime) BETWEEN DATE(?) AND DATE(?)
                                AND (Party1ID = ? OR Party2ID = ?)
                            '''
                result = \
                    cursor.execute(query, (Start_Date, End_Date, GeneratedByUserID, GeneratedByUserID)).fetchone()[0]
            elif ReportType == 'TransactionCount':
                query = '''
                                SELECT COUNT(TransactionID) AS Result
                                FROM Transactions
                                WHERE date(TransactionDateTime) BETWEEN DATE(?) AND DATE(?)
                                AND (Party1ID = ? OR Party2ID = ?)
                            '''
                result = \
                    cursor.execute(query, (Start_Date, End_Date, GeneratedByUserID, GeneratedByUserID)).fetchone()[0]
            elif ReportType in ('Sum_Category', 'Count_Category'):
                category = 'your_category'  # Replace with your actual category
                query = f'''
                                SELECT {ReportType}(Amount) AS Result
                                FROM Transactions
                                WHERE date(TransactionDateTime) BETWEEN DATE(?) AND DATE(?)
                                AND (Party1ID = ? OR Party2ID = ?)
                                AND Category = ?
                            '''
                result = cursor.execute(query, (
                    Start_Date, End_Date, GeneratedByUserID, GeneratedByUserID, category)).fetchone()[0]
            elif ReportType == 'Sum_Amount':
                query = '''
                                SELECT SUM(Amount) AS Result
                                FROM Transactions
                                WHERE date(TransactionDateTime) BETWEEN DATE(?) AND DATE(?)
                                AND (Party1ID = ? OR Party2ID = ?)
                            '''
                result = \
                    cursor.execute(query, (Start_Date, End_Date, GeneratedByUserID, GeneratedByUserID)).fetchone()[0]
            else:
                result = None
                ReportName = cursor.execute(query).fetchall()
                GeneratedDateTime = datetime.datetime.now()

            ReportType = 'Please Enter Valid Value' if result is None else result[0]

            ReportType = 'No Transaction' if ReportType is None else ReportType

            reports = Reports(i, ReportName, ReportType, GeneratedByUserID, GeneratedDateTime)

            cursor.execute('''
            insert into Reports (ReportID,ReportName,ReportType,GeneratedByUserID,GeneratedDateTime             
            ''', (reports.ReportID, reports.ReportName, reports.ReportType,
                  reports.GeneratedByUserID, reports.GeneratedDateTime))
    except sqlite3.Error as e:
        print(f' Iteration Error as {i} : {e}')


# New User Registration Endpoint
@app.route('/NewUser', methods=['POST'])
def NewUser():
    with sqlite3.connect('tms.db') as connection:
        cursor = connection.cursor()
        cursor.execute('select max(UserID) from Users')
        latest_user_id = cursor.fetchone()[0]
        new_user_id = latest_user_id + 1 if latest_user_id is not None else 3
        Username = request.args.get('Username')
        Password = request.args.get('Password')
        role = 'Dummy Users'
        user = SystemUsers(new_user_id, Username, Password, role)
        cursor.execute("insert into Users (UserID,Username,Password,UserRole) values(?,?,?,?)",
                       (user.UserID, user.Username, user.Password, user.UserRole))
        return 'New User Added Successfully'


@app.route('/admin_login', methods=['POST'])
def admin_data():
    try:
        input_username = request.form.get('Username')
        input_password = request.form.get('Password')
        if input_username == 'admin' and input_password == 'admin123':
            return redirect(url_for('admin_dashboard'))
        else:
            app.logger.warning('Invalid Credentials For Admin')
            return 'Invalid Credentials For Admin'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'An error occurred while processing your request'


@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
    try:
        return '''
            <h1>Welcome to Admin Dashboard</h1>
            <ul>
                <li><a href="/admin_dummyusers">Generate Dummy Users</a></li>
                <li><a href="/admin_dummytransactions">Generate Dummy Transactions</a></li>
                <li><a href="/admin_dummy_rule">Generate Dummy Rule</a></li>
                <li><a href="/admin_dummy_audittrail">Generate Dummy AuditTrails</a></li> 
                <li><a href="/admin_showdata">Show Users</a></li>
                <li><a href="/admin_showtransactions">Show Transactions</a></li>
                <li><a href="/admin_showtransactionrules">Show Transaction Rules</a></li> 
                <li><a href="/admin_showaudittrails">Show Audit Trails</a></li> 
            </ul>
        '''
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'An error occurred while processing your request'


@app.route('/admin_dummyusers', methods=['POST'])
def admin_dummyusers():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(UserID) from Users')
            latest_user_id = cursor.fetchone()[0]
            new_user_id = latest_user_id + 1 if latest_user_id is not None else 3
            Username = request.form.get('Username')
            Password = request.form.get('Password')
            role = 'Dummy Users'
            user = SystemUsers(new_user_id, Username, Password, role)
            cursor.execute("insert into Users (UserID,Username,Password,UserRole) values(?,?,?,?)",
                           (user.UserID, user.Username, user.Password, user.UserRole))
            return 'New User Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/admin_dummytransactions', methods=['POST'])
def admin_dummytransactions():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(TransactionID) from Transactions')
            latest_transaction = cursor.fetchone()[0]
            new_transaction = latest_transaction + 1 if latest_transaction else 1
            TransactionDateTime = datetime.datetime.now()
            Transactiontype = request.form.get('Transactiontype')
            Amount = request.form.get('Amount')
            Party1ID = request.form.get('Party1ID')
            Party2ID = request.form.get('Party2ID')
            TransactionStatus = request.form.get('TransactionStatus')
            Category = request.form.get('Category')
            Comments = request.form.get('Comments')

            transactions = Transactions(new_transaction, TransactionDateTime, Transactiontype, Amount,
                                        Party1ID, Party2ID, TransactionStatus, Category, Comments)
            cursor.execute('''
            insert into Transactions (TransactionID,TransactionDateTime,
            Transactiontype,Amount,Party1ID,Party2ID,
            TransactionStatus,Category,Comments) values 
            (?,?,?,?,?,?,?,?,?)''', (
                transactions.TransactionID, transactions.TransactionDateTime, transactions.Transactiontype,
                transactions.Amount, transactions.Party1ID, transactions.Party2ID, transactions.TransactionStatus,
                transactions.Category, transactions.Comments))
            return 'Dummy Transaction Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/admin_dummy_rule', methods=['POST'])
def admin_dummy_rule():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(RuleID) from TransactionsRules')
            latest_ruleid = cursor.fetchone()[0]
            new_ruleid = latest_ruleid + 1 if latest_ruleid else 1
            RuleName = request.form.get('RuleName')
            ruledescription = {
                'Sum_Credit': ['Will Provide Sum Of Credited Transaction on The Basis of Transaction User'],
                'Sum_Debit': ['Will Provide Sum Of Debited Transaction on The Basis of Transaction User'],
                'Count_Credit': ['Will Provide Count Of Credited Transaction on The Basis of Transaction User'],
                'Count_Debit': ['Will Provide Count Of Debited Transaction of Basis on The Transaction User']
            }
            RuleDescription = random.choice(ruledescription.get(RuleName, ['Not Defined Description']))
            UserID = request.form.get('UserID')

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                    From Transactions
                    INNER JOIN Users on Users.UserID = Transactions.Party1ID or 
                    Users.UserID = Transactions.Party2ID
                    WHERE 
                '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += "and Users.UserID = {}".format(UserID)

            result = cursor.execute(query_rule).fetchone()

            ValidationQuery = 'Please Enter Valid Value' if result is None else result[0]

            ValidationQuery = 'Please Enter Valid Value' if ValidationQuery is None else ValidationQuery

            transactionsrules = TransactionsRules(new_ruleid, RuleName, RuleDescription, ValidationQuery, UserID)
            cursor.execute('''
            insert into TransactionsRules (RuleID,RuleName,RuleDescription,ValidationQuery,UserID)
            values(?,?,?,?,?)
            ''', (transactionsrules.RuleID, transactionsrules.RuleName, transactionsrules.RuleDescription,
                  transactionsrules.ValidationQuery, transactionsrules.UserID))
        return 'Dummy Transaction Rule Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/admin_dummy_audit', methods=['POST'])
def admin_dummy_audit():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(AuditID) from AuditTrail')
            latest_auditid = cursor.fetchone()[0]
            new_auditid = latest_auditid + 1 if latest_auditid else 1
            UserID = request.form.get('UserID')
            TransactionID = request.form.get('TransactionID')
            RuleName = request.form.get('RuleName')
            one_year_ago = fake.date_time_between(start_date='-1y', end_date='now')
            Start_Date = one_year_ago
            End_Date = (one_year_ago + datetime.timedelta(days=random.randint(1, 365)))
            ActionBy = request.form.get(
                'ActionBy')  # there go time in format of  "2023-04-24 09:48:29 to 2023-05-29 09:48:29"

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                           FROM Transactions
                            INNER JOIN AuditTrail ON AuditTrail.UserID = Transactions.Party1ID OR 
                            AuditTrail.UserID = Transactions.Party2ID
                            WHERE 
                        '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f" AND AuditTrail.UserID = {UserID} AND date(Transactions.TransactionDateTime) BETWEEN DATE('{Start_Date}') AND DATE('{End_Date}')"

                result = cursor.execute(query_rule).fetchone()

                ActionPerformed = 'Please Enter Valid Value' if result is None else result[0]

                ActionPerformed = 'No Transaction' if ActionPerformed is None else ActionPerformed
            if ActionBy:
                cursor.execute('''
                        select * from Transactions
                        inner join AuditTrail on AuditTrail.UserID = Transactions.Party1ID
                        or AuditTrail.UserID = Transactions.Party2ID
                        where date(Transactions.TransactionDateTime) BETWEEN DATE(?) AND DATE(?) 
                        and UserID = ?
                        ''', (Start_Date, End_Date, UserID,)).fetchall()

            ActionTimestamp = datetime.datetime.now()
            audittrail = AuditTrail(new_auditid, UserID, TransactionID, ActionBy, RuleName, ActionPerformed,
                                    ActionTimestamp)
            cursor.execute('''
                        INSERT INTO AuditTrail
                        (AuditID, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                audittrail.AuditID, audittrail.UserID, audittrail.TransactionID, audittrail.ActionBy,
                audittrail.RuleName, audittrail.ActionPerformed, audittrail.ActionTimestamp))
            return 'Audit Trail Added Successfully'
    except sqlite3.Error as e:
        print(f'The Iteration Error : {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/admin_showdata', methods=['GET'])
def admin_showdata():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/admin_showtransactions', methods=['GET'])
def admin_showtransactions():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Transactions')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/admin_showtransactionrules', methods=['GET'])
def admin_showtransactionrules():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM TransactionsRules')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/admin_showaudittrails', methods=['GET'])
def admin_showaudittrails():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select * from AuditTrail')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


def is_admin(Username, Password):
    return Username == 'admin' and Password == 'admin123'


@app.route('/manager_login', methods=['POST'])
def manager():
    try:
        input_username = request.form.get('Username')
        input_password = request.form.get('Password')
        if input_username == 'manager' and input_password == 'manager123':
            return redirect(url_for('manager_dashboard'))
        else:
            app.logger.warning('Invalid Credentials For Manager')
            return 'Invalid Credentials For Manager'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'An error occurred while processing your request'


@app.route('/manager_dashboard', methods=['GET'])
def manager_dashboard():
    try:
        return '''
            <h1>Welcome to Manager Dashboard</h1>
            <ul>
                <li><a href="/manager_dummyusers">Generate Dummy Users</a></li>
                <li><a href="/manager_dummytransactions">Generate Dummy Transactions</a></li>
                <li><a href="/manager_dummy_rule">Generate Dummy Rule</a></li>
                <li><a href="/manager_dummy_audittrail">Generate Dummy AuditTrails</a></li> 
                <li><a href="/manager_showdata">Show Users</a></li>
                <li><a href="/manager_showtransactions">Show Transactions</a></li>
                <li><a href="/manager_showtransactionrules">Show Transaction Rules</a></li>
                <li><a href="/manager_showaudittrails">Show Audit Trails</a></li>  
            </ul>
        '''
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'An error occurred while processing your request'


@app.route('/manager_dummyusers', methods=['POST'])
def manager_dummyusers():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(UserID) from Users')
            latest_user_id = cursor.fetchone()[0]
            new_user_id = latest_user_id + 1 if latest_user_id is not None else 3
            Username = request.form.get('Username')
            Password = request.form.get('Password')
            role = 'Dummy Users'
            user = SystemUsers(new_user_id, Username, Password, role)
            cursor.execute("insert into Users (UserID,Username,Password,UserRole) values(?,?,?,?)",
                           (user.UserID, user.Username, user.Password, user.UserRole))
            return 'New User Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/manager_dummytransactions', methods=['POST'])
def manager_dummytransactions():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(TransactionID) from Transactions')
            latest_transaction = cursor.fetchone()[0]
            new_transaction = latest_transaction + 1 if latest_transaction else 1
            TransactionDateTime = datetime.datetime.now()
            Transactiontype = request.form.get('Transactiontype')
            Amount = request.form.get('Amount')
            Party1ID = request.form.get('Party1ID')
            Party2ID = request.form.get('Party2ID')
            TransactionStatus = request.form.get('TransactionStatus')
            Category = request.form.get('Category')
            Comments = request.form.get('Comments')

            transactions = Transactions(new_transaction, TransactionDateTime, Transactiontype, Amount,
                                        Party1ID, Party2ID, TransactionStatus, Category, Comments)
            cursor.execute('''insert into Transactions (TransactionID,TransactionDateTime,Transactiontype,Amount,Party1ID,Party2ID,
            TransactionStatus,Category,Comments) values (?,?,?,?,?,?,?,?,?)''', (
                transactions.TransactionID, transactions.TransactionDateTime, transactions.Transactiontype,
                transactions.Amount,
                transactions.Party1ID, transactions.Party2ID, transactions.TransactionStatus, transactions.Category,
                transactions.Comments))
            return 'Dummy Transaction Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/manager_dummy_rule', methods=['POST'])
def manager_dummy_rule():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(RuleID) from TransactionsRules')
            latest_ruleid = cursor.fetchone()[0]
            new_ruleid = latest_ruleid + 1 if latest_ruleid else 1
            RuleName = request.form.get('RuleName')
            ruledescription = {
                'Sum_Credit': ['Will Provide Sum Of Credited Transaction on The Basis of Transaction User'],
                'Sum_Debit': ['Will Provide Sum Of Debited Transaction on The Basis of Transaction User'],
                'Count_Credit': ['Will Provide Count Of Credited Transaction on The Basis of Transaction User'],
                'Count_Debit': ['Will Provide Count Of Debited Transaction of Basis on The Transaction User']
            }
            RuleDescription = random.choice(ruledescription.get(RuleName, ['Not Defined Description']))
            UserID = random.randint(2, 101)

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                    From Transactions
                    INNER JOIN Users on Users.UserID = Transactions.Party1ID or 
                    Users.UserID = Transactions.Party2ID
                    WHERE 
                '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f"and Users.UserID = {UserID}"

            result = cursor.execute(query_rule).fetchone()

            ValidationQuery = 'Please Enter Valid Value' if result is None else result[0]

            ValidationQuery = 'Please Enter Valid Value' if ValidationQuery is None else ValidationQuery

            transactionsrules = TransactionsRules(new_ruleid, RuleName, RuleDescription, ValidationQuery, UserID)
            cursor.execute('''
            insert into TransactionsRules (RuleID,RuleName,RuleDescription,ValidationQuery,UserID)
            values(?,?,?,?,?)
            ''', (transactionsrules.RuleID, transactionsrules.RuleName, transactionsrules.RuleDescription,
                  transactionsrules.ValidationQuery, transactionsrules.UserID))
            return 'Dummy Transaction Rule Added Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/manager_dummy_audittrail', methods=['POST'])
def manager_dummy_audittrail():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(AuditID) from AuditTrail')
            latest_auditid = cursor.fetchone()[0]
            new_auditid = latest_auditid + 1 if latest_auditid else 1
            UserID = request.form.get('UserID')
            TransactionID = request.form.get('TransactionID')
            RuleName = request.form.get('RuleName')
            one_year_ago = fake.date_time_between(start_date='-1y', end_date='now')
            Start_Date = one_year_ago
            End_Date = (one_year_ago + datetime.timedelta(days=random.randint(1, 365)))
            ActionBy = request.form.get(
                'ActionBy')  # there go time in format of  "2023-04-24 09:48:29 to 2023-05-29 09:48:29"

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                           FROM Transactions
                            INNER JOIN AuditTrail ON AuditTrail.UserID = Transactions.Party1ID OR 
                            AuditTrail.UserID = Transactions.Party2ID
                            WHERE 
                        '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f" AND AuditTrail.UserID = {UserID} AND date(Transactions.TransactionDateTime) BETWEEN DATE('{Start_Date}') AND DATE('{End_Date}')"

                result = cursor.execute(query_rule).fetchone()

                ActionPerformed = 'Please Enter Valid Value' if result is None else result[0]

                ActionPerformed = 'No Transaction' if ActionPerformed is None else ActionPerformed
            if ActionBy:
                cursor.execute('''
                        select * from Transactions
                        inner join AuditTrail on AuditTrail.UserID = Transactions.Party1ID
                        or AuditTrail.UserID = Transactions.Party2ID
                        where date(Transactions.TransactionDateTime) BETWEEN DATE(?) AND DATE(?) 
                        and UserID = ?
                        ''', (Start_Date, End_Date, UserID,)).fetchall()

            ActionTimestamp = datetime.datetime.now()
            audittrail = AuditTrail(new_auditid, UserID, TransactionID, ActionBy, RuleName, ActionPerformed,
                                    ActionTimestamp)
            cursor.execute('''
                        INSERT INTO AuditTrail
                        (AuditID, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                audittrail.AuditID, audittrail.UserID, audittrail.TransactionID, audittrail.ActionBy,
                audittrail.RuleName, audittrail.ActionPerformed, audittrail.ActionTimestamp))
            return 'Audit Trail Added Successfully'
    except sqlite3.Error as e:
        print(f'The Iteration Error : {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/manager_showdata', methods=['GET'])
def manager_showdata():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users where UserID >= 2')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/manager_showtransactions', methods=['GET'])
def manager_showtransactions():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Transactions 
                           where Transactions.Party1ID >= 2 and
                           Transactions.Party2ID >= 2                           
                           ''')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/manager_showtransactionrules', methods=['GET'])
def manager_showtransactionrules():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM TransactionsRules where UserID >= 2')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/manager_showaudittrails', methods=['GET'])
def manager_showaudittrails():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * from AuditTrail where UserID >= 2')
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


def is_manager(Username, Password):
    return Username == 'manager' and Password == 'manager123'


@app.route('/user_login', methods=['POST'])
def user_login():
    global user
    try:
        input_username = request.form.get('Username')
        input_password = request.form.get('Password')
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                            select * 
                            from Users where 
                            Username = ? and Password = ?      
                            ''', (input_username, input_password))
            user_data = cursor.fetchone()
        if user_data is None or user_data[3] != 'User':
            return 'Invalid Credentials No Data Found'
        else:
            user = SystemUsers(*user_data)
            app.logger.debug(f'User  {input_username} logged in successfully')
            return redirect(url_for('user_dashboard'))
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'An Error occurred while processing your request'


@app.route('/user_dashboard', methods=['GET'])
def user_dashboard():
    try:
        return '''
            <h1> Welcome to User DashBoard</h1>
            <ul>
            <li><a href='/user_showdata'>Show Users</a></li>
            <li><a href='/user_showtransactions'>Show Transactions</a></li>
            <li><a href ='/user_showtransactionrules'>Show Transaction Rules</a></li>
            <li><a href="/user_showaudittrails">Show Audit-Trails</a></li> 
            <li><a href ='/NewTransaction'>New Transaction</a></li>
            <li><a href ='/NewTransactionRule'>New Transaction Rule</a></li>
            <li><a href="/NewAuditTrail">Create New Audit-Trails</a></li>  
            </ul>
        '''
    except Exception as e:
        print(f'An Error Occurred : {e}')
        return 'An error occurred while processing you request'


@app.route('/user_showdata', methods=['GET'])
def user_showdata():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Users where UserID = ?', (user.UserID,))
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/user_showtransactions', methods=['GET'])
def user_showtransactions():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT * FROM Transactions
            WHERE Transactions.Party1ID = ? or Transactions.Party2ID = ?
                        ''', (user.UserID, user.UserID,))
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/user_showtransactionrules', methods=['GET'])
def user_showtransactionrules():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT * FROM TransactionsRules where UserID = ?
            ''', (user.UserID,))
            result = cursor.fetchmany()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/user_showaudittrails', methods=['GET'])
def user_showaudittrails():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * from AuditTrail where UserID = ?', (audittrail.UserID,))
            result = cursor.fetchall()
        return jsonify({'result': result})
    except sqlite3.Error as e:
        app.logger.error(f'Database Error: {e}')
        return 'Error occurred while accessing the database', 500


@app.route('/NewTransaction', methods=['POST'])
def NewTransaction():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(TransactionID) from Transactions')
            latest_transaction = cursor.fetchone()[0]
            new_transaction = latest_transaction + 1 if latest_transaction else 1
            TransactionDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            Transactiontype = request.form.get('Transactiontype')
            Amount = request.form.get('Amount')
            Party1ID = request.form.get('Party1ID')
            Party2ID = request.form.get('Party2ID')
            TransactionStatus = request.form.get('TransactionStatus')
            Category = request.form.get('Category')
            Comments = request.form.get('Comments')

            transactions = Transactions(new_transaction, TransactionDateTime, Transactiontype, Amount,
                                        Party1ID, Party2ID, TransactionStatus, Category, Comments)
            cursor.execute('''insert into Transactions (TransactionID,TransactionDateTime,Transactiontype,Amount,Party1ID,Party2ID,
            TransactionStatus,Category,Comments) values (?,?,?,?,?,?,?,?,?)''', (
                transactions.TransactionID, transactions.TransactionDateTime, transactions.Transactiontype,
                transactions.Amount,
                transactions.Party1ID, transactions.Party2ID, transactions.TransactionStatus, transactions.Category,
                transactions.Comments))
            return 'Transaction Made Successfully'
    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


@app.route('/NewTransactionRule', methods=['POST'])
def NewTransactionRule():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(RuleID) from TransactionsRules')
            latest_ruleid = cursor.fetchone()[0]
            new_ruleid = latest_ruleid + 1 if latest_ruleid else 1
            RuleName = request.form.get('RuleName')
            ruledescription = {
                'Sum_Credit': ['Will Provide Sum Of Credited Transaction on The Basis of Transaction User'],
                'Sum_Debit': ['Will Provide Sum Of Debited Transaction on The Basis of Transaction User'],
                'Count_Credit': ['Will Provide Count Of Credited Transaction on The Basis of Transaction User'],
                'Count_Debit': ['Will Provide Count Of Debited Transaction of Basis on The Transaction User']
            }
            RuleDescription = ', '.join(ruledescription.get(RuleName, ['Not Defined Description']))
            UserID = request.form.get('UserID')

            if RuleName is not None and UserID is not None:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                    From Transactions
                    INNER JOIN Users on Users.UserID = Transactions.Party1ID or 
                    Users.UserID = Transactions.Party2ID
                    WHERE 
                '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += "and Users.UserID = {}".format(UserID)

                ValidationQuery = cursor.execute(query_rule).fetchone()[0]

                ValidationQuery = 'Please Enter Valid Value' if ValidationQuery is None else ValidationQuery

                transactionsrules = TransactionsRules(new_ruleid, RuleName, RuleDescription, ValidationQuery, UserID)
                cursor.execute('''
                insert into TransactionsRules (RuleID,RuleName,RuleDescription,ValidationQuery,UserID)
                values(?,?,?,?,?)
                ''', (transactionsrules.RuleID, transactionsrules.RuleName, transactionsrules.RuleDescription,
                      transactionsrules.ValidationQuery, transactionsrules.UserID))
                return 'Transaction Rule Added Successfully'
            else:
                return 'Invalid input data', 400

    except sqlite3.Error as e:
        print(f'Database Error {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred', 500


@app.route('/NewAuditTrail', methods=['POST'])
def NewAuditTrail():
    try:
        with sqlite3.connect('tms.db') as connection:
            cursor = connection.cursor()
            cursor.execute('select max(AuditID) from AuditTrail')
            latest_auditid = cursor.fetchone()[0]
            new_auditid = latest_auditid + 1 if latest_auditid else 1
            UserID = request.form.get('UserID')
            TransactionID = request.form.get('TransactionID')
            RuleName = request.form.get('RuleName')
            one_year_ago = fake.date_time_between(start_date='-1y', end_date='now')
            Start_Date = one_year_ago
            End_Date = (one_year_ago + datetime.timedelta(days=random.randint(1, 365)))
            ActionBy = request.form.get(
                'ActionBy')  # there go time in format of  "2023-04-24 09:48:29 to 2023-05-29 09:48:29"

            if RuleName:
                if RuleName.startswith('Sum'):
                    query_rule = 'SELECT SUM(Transactions.Amount)'
                elif RuleName.startswith('Count'):
                    query_rule = 'SELECT COUNT(Transactions.Amount)'

                query_rule += '''
                       FROM Transactions
                        INNER JOIN AuditTrail ON AuditTrail.UserID = Transactions.Party1ID OR 
                        AuditTrail.UserID = Transactions.Party2ID
                        WHERE 
                    '''
                if RuleName.endswith('_Credit'):
                    query_rule += 'Transactions.Transactiontype = "Credit"'
                elif RuleName.endswith('_Debit'):
                    query_rule += 'Transactions.Transactiontype = "Debit"'

                if RuleName.startswith('Sum') or RuleName.startswith('Count'):
                    query_rule += f" AND AuditTrail.UserID = {UserID} AND date(Transactions.TransactionDateTime) BETWEEN DATE('{Start_Date}') AND DATE('{End_Date}')"

                result = cursor.execute(query_rule).fetchone()

                ActionPerformed = 'Please Enter Valid Value' if result is None else result[0]

                ActionPerformed = 'No Transaction' if ActionPerformed is None else ActionPerformed
            if ActionBy:
                cursor.execute('''
                    select * from Transactions
                    inner join AuditTrail on AuditTrail.UserID = Transactions.Party1ID
                    or AuditTrail.UserID = Transactions.Party2ID
                    where date(Transactions.TransactionDateTime) BETWEEN DATE(?) AND DATE(?) 
                    and UserID = ?
                    ''', (Start_Date, End_Date, UserID,)).fetchall()

            ActionTimestamp = datetime.datetime.now()
            audittrail = AuditTrail(new_auditid, UserID, TransactionID, ActionBy, RuleName, ActionPerformed,
                                    ActionTimestamp)
            cursor.execute('''
                    INSERT INTO AuditTrail
                    (AuditID, UserID, TransactionID, ActionBy, RuleName, ActionPerformed, ActionTimestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                audittrail.AuditID, audittrail.UserID, audittrail.TransactionID, audittrail.ActionBy,
                audittrail.RuleName, audittrail.ActionPerformed, audittrail.ActionTimestamp))
            return 'Audit Trail Added Successfully'
    except sqlite3.Error as e:
        print(f'The Iteration Error : {e}')
        return 'Error occurred while accessing the database', 500
    except Exception as e:
        app.logger.error(f'An Unexpected error occurred: {e}')
        return 'An unexpected error occurred'


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, port=5001)
