import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Salesperson-card.component.html',
  styleUrls: ['./Salesperson-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Salesperson-card]': 'true'
  }
})

export class SalespersonCardComponent {


}