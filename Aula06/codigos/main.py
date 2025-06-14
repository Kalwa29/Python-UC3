from conta import ContaCorrente

contas={
    '123':ContaCorrente('Saulo Kalwa', '123', 'Sas123', 100.0),
    '456':ContaCorrente('Josué', '456', 'jegue_rico',200.0)
}

ContaCorrente.mostrar_saldo(contas['123'])