import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Warranty-card.component.html',
  styleUrls: ['./Warranty-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Warranty-card]': 'true'
  }
})

export class WarrantyCardComponent {


}