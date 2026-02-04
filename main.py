from funzioni_supporto import scelta

#Per funzionare create un database con nome es: "Db_azienda"

#E creare l'unica tabella richiesta fattura -> presente in script_sql.py

#Opzionalmente (pro): creare un file python "genera_tabella.py" che richiama quello script e lo esegue
#direttamente sul nostro Database, andando quindi a creare la tabella.

#permettere all'utente di inserire una nuova fattura, stando MOLTO attenti agli id sequenziali e
#a tutto ciò che non deve essere NULL. Inoltre pensate se riuscite ad inserire alcuni dei campi in
#automatico (imponibile, data, ecc)

if __name__ == '__main__':
    scelta()