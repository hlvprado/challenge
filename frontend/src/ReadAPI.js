import React from 'react';
import './ReadAPI.css';

class ReadAPI extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        items: []
      };
    }
  
    componentDidMount() {
      const current = new Date();
      var date = current.getDate() + "/"  + (current.getMonth() + 1) + "/" + current.getFullYear();
      var lastYear = current.getDate() + "/"  + (current.getMonth() + 1) + "/" + (current.getFullYear() - 1);
      fetch("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=" + lastYear + "&dataFinal=" + date)
        .then(res => res.json())
        .then(
          (results) => {
            var dataSum = 0;
            for(let i = 0; i < results.length; i++) {
              dataSum += parseFloat(results[i].valor);
            }
            let resultSum = [{"id": 0, "start_date": lastYear, "end_date": date, "data_sum": dataSum}]
            this.setState({
              isLoaded: true,
              items: resultSum
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
  
    render() {
      const { error, isLoaded, items } = this.state;
      if (error) {
        return <div>Erro: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Carregando...</div>;
      } else {
        return (
          <div>
            <ul>
              {items.map(item => (
                <li key={item.id}>
                  <span key={item.id+1}>O resultado da soma para o período entre {item.start_date} e {item.end_date} é <b>{item.data_sum}</b></span>
                </li>
              ))}
            </ul>
          </div>
        );
      }
    }
  }

  export default ReadAPI;