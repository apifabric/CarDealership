import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Repair-card.component.html',
  styleUrls: ['./Repair-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Repair-card]': 'true'
  }
})

export class RepairCardComponent {


}