import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Sale-card.component.html',
  styleUrls: ['./Sale-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Sale-card]': 'true'
  }
})

export class SaleCardComponent {


}